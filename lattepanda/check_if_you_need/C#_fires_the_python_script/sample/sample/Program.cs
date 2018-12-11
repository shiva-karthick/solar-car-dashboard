using System;
using System.Diagnostics;
using System.IO;

namespace sample
{
    class Program
    {
        static void Main(string[] args)
        {
            string progToRun = "C:\\Users\\Asha\\Desktop\\solar-car-dashboard\\Lattepanda\\communicate_arduino_lattepanda\\C#_fires_the_python_script\\sample.py";
            char[] spliter = { '\r' };

            Process proc = new Process();
            proc.StartInfo.FileName = "python.exe";
            proc.StartInfo.RedirectStandardOutput = true;
            proc.StartInfo.UseShellExecute = false;

            // call hello.py to concatenate passed parameters
            proc.StartInfo.Arguments = string.Concat(progToRun);
            proc.Start();

            StreamReader sReader = proc.StandardOutput;
            string[] output = sReader.ReadToEnd().Split(spliter);

            foreach (string s in output)
                Console.WriteLine(s);

            proc.WaitForExit();

            Console.ReadLine();

        }


    }

}
