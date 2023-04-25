import subprocess
import tkinter as tk
from tkinter import filedialog

def compile_code():

    # Get input text from the Text widget
    source_code = input_text.get(1.0, tk.END).strip() 

    # Write the input Java code to a temporary file
    # with open('temp.java', 'w') as f:
    #     f.write(source_code)


        # Replace the command and arguments with your custom compiler command and arguments
    compiler_command = "my_custom_compiler"
    compiler_arguments = ["-o", "output_file", "-c", "-"]
    
    try:
        # Create a subprocess to run the compiler
        process = subprocess.Popen([compiler_command] + compiler_arguments,
                                   stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE, universal_newlines=True)
        # Send the Java source code to the compiler as input
        process.stdin.write(source_code)
        process.stdin.close()

        # Capture the output and error messages from the compiler
        output = process.stdout.read()
        error_output = process.stderr.read()

        # Update the output Text widget with the compiler's output and error messages
        output_text.configure(state=tk.NORMAL)
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, output)
        output_text.insert(tk.END, error_output)
        output_text.configure(state=tk.DISABLED)

    except Exception as e:
        output_text.configure(state=tk.NORMAL)
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, "Compilation error: " + str(e))
        output_text.configure(state=tk.DISABLED)


# Create the Tkinter window
root = tk.Tk()
root.title("Java Compiler")

# Create a frame for input code
input_frame = tk.Frame(root)
input_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Create the input Text widget inside the input frame
input_text = tk.Text(input_frame, height=20, width=50)
input_text.pack(fill=tk.BOTH, expand=True)

# Create a frame for output result
result_frame = tk.Frame(root)
result_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

# Create the result Text widget inside the result frame
output_text = tk.Text(result_frame, height=20, width=50)
output_text.pack(fill=tk.BOTH, expand=True)
output_text.configure(state='disabled')

# Create the compile button
compile_button = tk.Button(input_frame, text="Compile", command=compile_code, compound="center", borderwidth=0)
compile_button.pack(pady=10)

root.mainloop()

