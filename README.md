# L&K FoodHouse POS System

#### Video Demo: https://youtu.be/Mkjd7XZrR-0 

#### Description
Hello! This is my final project for my CS50p course. I decided to make a simple POS system specifically designed for the needs of L&K FoodHouse, my brother's newly opened food establishment in our small province in the Philippines. The program provides a simple and interative interface for managing orders, calculating totals and change and generating sales reports. The system is built using the new CustomTKinter library, a modern GUI for python for enhanced user experience, making it usable on the counter or even at the customer's table (since I plan to deploy this on an android tablet).

   > I'm so happy and proud with this! I'm so thankful to Professor David and Harvard for these amazing course that are unbelievably free! This is my first ever personal program, and I tried to integrate as much things I have learned, and particularly decided to structure the program into an OOP since it was a struggle for me to wrap my head around the subject, hoping that working with it can make my understanding of the thing better. But it was hard and confusing, the routing, passing, constructor, dunder, I still don't understand them fully. But so far, the program is working according to how I want it to be. And the hardest challenge is the integration 'CustomTKinter' library, which I never had any experience with, or even heard in the course. But as a person who likes seeing the progress on what he's working on, playing with GUI made the project more fun to me. Making decisions on the widget's colors, size, positions was time consuming since I was doing it in trial and error, but eventually landed on a look I am happy with. 
   
   > There's still a lot to add and fix though, one is making the card payment work. At the moment it's just a visual accessory, but soon, after learning more about API, PCI, etc., that feature will be available. But since my brother's resto doesn't require it (in the Philippines rural areas, cash is still the thing), the program is good for my project. And yes, I mentioned that I plan to run this on android for easier access, a POS that can be used as a Menu selection for customers as well. Hence, adding images too. I'm excited! 
   
   > I have learned so much on this project, and the whole course. I'm really thankful for Professor David and Harvard. God-willing, this humble project will be the start of a better thing for a college undergraduate such as me.


## Main Features

- **Menu Category Display** View and choose your food items categorized by type with an easy-to-mavigate interface.
- **Choose Food Items Display** Clicking the Menu buttons category shows the Food items accordingly. By clicking the desired item, you choose the item, and each click adds to the quantity + 1.
- **Selected Items Display** Selected food items are added and are displayed with their quantity, with a real time Subtotal Display at the bottom of the screen.
- **Remove Items / Reset Selection Button** Remove a specific item by highlighting the name of the item, every Click of the Remove Item button decrements the quantity by 1, or reset all of the selection by the Reset Selection Button.
- **Checkout Button** Calculates the total bill, and provides options for payment via cash or card, and generates change for cash transactions.
- **Sales Report** A sales report is automatically generated in the "Sales.txt" file that includes the date, items, quantity, and total sales.
- **Easy-to-update Menu database** The programs reads the the whole menu from a "menu.json" file, and automatically assigns the category and food items accordingly.

## Appearance Mode

- Easily switch between light and dark appearance modes using a segmented button at the upper left corner of the window.

## Requirements
> A complete list is listed in the requirements.txt 

- Python 3.x
- 'customTKinter' library
- 'TKinter' library

> [!IMPORTANT]
> When running this in your IDE, or running the '.exe' version, please make sure that you have a 'menu.json' file within the folder containing the script or executable, otherwise, the program won't work.
   > [!IMPORTANT]
   > The file should be STRICTLY structured as follows:
  ```json
   {
       "category": {
           "item": 10.99,
           "item": 8.49
       },

       "new category": {
           "item_a": 10.99,
           "item_b": 8.49
       }
   }
   ```

## Customization
- **Menu Configuration** Customize the 'menu.json' according to your needs. Ensure that the file follows the correct JSON format.
> [!NOTE]
> The contents of the 'menu.json' should :
* all be written in lower case
* use underscore '_' instead of space ' ' as word separators on food item names.
* food items are indented under the category



