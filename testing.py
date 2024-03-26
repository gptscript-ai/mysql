import os
import string
import subprocess


workdir = "< path to repo >"


def run_command(command, output_file):
    # Open a file to write the output
    output_file = open(workdir + "testing/" + output_file, "w")

    # Run the command `iter` times and record the output to the file
    for _ in range(10):
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        stdout, stderr = process.communicate()
        output_file.write(stdout.decode("utf-8") + "\n")
        output_file.write(stderr.decode("utf-8") + "\n")

    # Close the output file
    output_file.close()


def load_cache(command):
    process = subprocess.run(command, shell=True)


def get_file_names(directory, suffix):
    file_names = []
    for filename in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, filename)) and (suffix is None or filename.endswith(suffix)):
            file_names.append(filename)
    return file_names
    

def get_command(file_name, cache):
    if cache:
        return "time gptscript " + workdir + "examples/" + file_name
    return "time gptscript --cache=false " + workdir + "examples/" + file_name


# for each file we want to run a cache and a non cache version
def run_tests():
    files = get_file_names(workdir + "examples", ".gpt")
    for f in files:
        # non cached
        cmd = get_command(f, False)
        run_command(cmd, f[:-4]+"_no_cache.txt")

        # cached
        cmd = get_command(f, True)
        load_cache(cmd)
        run_command(cmd, f[:-4]+"_cache.txt")


def parse_files():
    command = "rg real " + workdir + "testing"
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    stdout, _ = process.communicate()

    output = ["workload","llama_no_cache","gpt_no_cache","llama_cache","gpt_cache"]
    outputDict = {}

    for line in stdout.decode("utf-8").split("\n"):
        l = line.split(":")
        if len(l) < 2:
            break
        file = l[0].split("/")[-1][:-4]
        time = l[1][l[1].index("m")+1:-1]

        # print(file, time)
        if file.startswith("llama_") and file.endswith("_no_cache"):
            key = file[len("llama_"):-len("_no_cache")]
            if key not in outputDict:
                outputDict[key] = {}
            if output[1] not in outputDict[key]:
                outputDict[key][output[1]] = []
            outputDict[key][output[1]].append(float(time))
        elif file.startswith("gpt_") and file.endswith("_no_cache"):
            key = file[len("gpt_"):-len("_no_cache")]
            if key not in outputDict:
                outputDict[key] = {}
            if output[2] not in outputDict[key]:
                outputDict[key][output[2]] = []
            outputDict[key][output[2]].append(float(time))
        elif file.startswith("llama_") and file.endswith("_cache"):
            key = file[len("llama_"):-len("_cache")]
            if key not in outputDict:
                outputDict[key] = {}
            if output[3] not in outputDict[key]:
                outputDict[key][output[3]] = []
            outputDict[key][output[3]].append(float(time))
        elif file.startswith("gpt_") and file.endswith("_cache"):
            key = file[len("gpt_"):-len("_cache")]
            if key not in outputDict:
                outputDict[key] = {}
            if output[4] not in outputDict[key]:
                outputDict[key][output[4]] = []
            outputDict[key][output[4]].append(float(time))

    # print(outputDict)
    for o in output:
        print(o, end=",")
    print()
    
    for workload in outputDict.keys():
        print(workload, end=",")
        curDict = outputDict[workload]
        for key in output[1:]:
            values = curDict[key]
            tot = 0
            for v in values:
                tot += v
            print(tot/len(values), end=",")
        print()



run_tests()
parse_files()
