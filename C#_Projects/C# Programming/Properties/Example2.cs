using System;  
   public class Employee  
    {  
        private string name;  
  
        public string Name  
        {  
            get  
            {  
                return name;  
            }  
            set  
            {  
                name = value+" JavaTpoint";  
                  
            }  
        }  
   }  
   class TestEmployee{  
       public static void Main(string[] args)  
        {  
            Employee e1 = new Employee();  
            e1.Name = "Sonoo";  
            Console.WriteLine("Employee Name: " + e1.Name);  
        }  
    }  