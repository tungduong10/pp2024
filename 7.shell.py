import os
import subprocess

def execute_command(command):
    try:
        if "|" in command:
            #handle piping
            processes=command.split("|")
            prev_process=None
            
            for i,pcs in enumerate(processes):
                args= pcs.strip().split()
                if i==0:   #1st cmd
                    prev_process=subprocess.Popen(args,stdout=subprocess.PIPE)
                elif i==len(pcs) -1:
                    #last cmd
                    output=subprocess.Popen(args,stdin=prev_process.stdout,capture_output=True,text=True)
                    prev_process.stdout.close()
                    return output.stdout
                else:
                    #middle cmds
                    prev_process=subprocess.Popen(args,stdin=prev_process.stdout,stdout=subprocess.PIPE)
            prev_process.stdout.close()
        elif ">" in command or "<" in command:
            parts=command.split("<") if "<" in command else command.split(">")
            left=parts[0].strip()
            right=parts[1].strip()
            
            if ">" in command:
                with open(right,"w") as outf:
                    subprocess.run(left.split(),stdout=outf)
            elif "<" in command:
                with open(right,'r') as inf:
                    return subprocess.run(left.split(),stdin=inf,capture_output=True,text=True).stdout
        else:
            #simple cmds
            return subprocess.run(command.split(" "),capture_output=True,text=True).stdout
    except Exception as e:
        return (f"Error: ",{str(e)})

if __name__=="__main__":
    while(True):
        try:
            user_input=input("$ ").strip()
            if user_input.lower() in ["exit","quit"]:
                break
            output=execute_command(user_input)
            if output:
                print(output)
        except KeyboardInterrupt as e:
            print("\nExiting shell...")
            break