using System;

namespace WildAnimalExample
{
    // Abstraction: Abstract class representing a general Wild Animal
    abstract class WildAnimal
    {
        // Encapsulation: Private field for animal's name
        private string name;
        
        // Constructor to initialize the name
        public WildAnimal(string name)
        {
            this.name = name;
        }

        // Property to get and set the name (Encapsulation)
        public string Name
        {
            get { return name; }
            set { name = value; }
        }

        // Abstract method to define the sound the animal makes
        public abstract void MakeSound();

        // Abstract method to describe the animal's behavior
        public abstract void Behavior();

        // Method to display the name of the animal
        public void DisplayInfo()
        {
            Console.WriteLine($"The animal's name is {Name}.");
        }
    }

    // Inheritance: Lion class inherits from WildAnimal
    class Lion : WildAnimal
    {
        // Constructor for Lion
        public Lion(string name) : base(name) { }

        // Polymorphism: Override MakeSound method for Lion
        public override void MakeSound()
        {
            Console.WriteLine($"{Name} roars: RAAWR!");
        }

        // Polymorphism: Override Behavior method for Lion
        public override void Behavior()
        {
            Console.WriteLine($"{Name} hunts for prey.");
        }
    }

    // Inheritance: Elephant class inherits from WildAnimal
    class Elephant : WildAnimal
    {
        // Constructor for Elephant
        public Elephant(string name) : base(name) { }

        // Polymorphism: Override MakeSound method for Elephant
        public override void MakeSound()
        {
            Console.WriteLine($"{Name} trumpets: PAAH! PAAH!");
        }

        // Polymorphism: Override Behavior method for Elephant
        public override void Behavior()
        {
            Console.WriteLine($"{Name} grazes and wanders in the savanna.");
        }
    }

    class Program
    {
        static void Main(string[] args)
        {
            // Create a Lion object
            Lion lion = new Lion("Simba");
            lion.DisplayInfo();  // Display the name of the animal
            lion.MakeSound();    // Display the sound made by the lion
            lion.Behavior();     // Display the behavior of the lion

            Console.WriteLine(); // Add a line break

            // Create an Elephant object
            Elephant elephant = new Elephant("Dumbo");
            elephant.DisplayInfo();  // Display the name of the animal
            elephant.MakeSound();    // Display the sound made by the elephant
            elephant.Behavior();     // Display the behavior of the elephant

            Console.ReadLine(); // Keep the console window open
        }
    }
}
