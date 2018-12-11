using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace second_step
{
    class Program
    {
        static void Main(string[] args)
        {
            
                Process send_values = Process.Start(new ProcessStartInfo("python.exe", "C:\\Users\\Asha\\Desktop\\solar-car-dashboard\\Lattepanda\\communicate_arduino_lattepanda\\second_step\\second_step.py")
                {
                RedirectStandardInput = true,
                UseShellExecute = false
                }
                );

            while (true)
            {
                send_values.StandardInput.WriteLine(string.Format("DATA,{0},{1},{2}", 25, 100, 75));
            }
        }
    }
}
