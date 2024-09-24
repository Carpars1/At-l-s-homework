from tkinter import *

# Create the window
window = Tk()
window.title("BMI Calculator")
window.minsize(width=250, height=350)

# Label for weight input
lb1 = Label(text="Please Enter your weight (kg)", font=("Times New Roman", 12, "normal"))
lb1.config(padx=25, pady=25)
lb1.pack()

# Entry for weight
entry1 = Entry(width=10)
entry1.pack()

# Label for height input
lb2 = Label(text="Please Enter your height (cm)", font=("Times New Roman", 12, "normal"))
lb2.config(padx=25, pady=25)
lb2.pack()

# Entry for height
entry2 = Entry(width=10)
entry2.pack()


# Function to calculate BMI and show the result
def click_the_button():
    try:
        user_entry1 = float(entry1.get())  # Weight in kg
        user_entry2 = float(entry2.get())  # Height in cm

        # Calculate BMI
        BMI = user_entry1 / ((user_entry2 / 100) ** 2)

        # Determine BMI category
        if BMI <= 18.5:
            result_text = "Underweight"
        elif 18.5 < BMI < 24.9:
            result_text = "Normal"
        elif 25 <= BMI < 29.9:
            result_text = "Overweight"
        elif 30 <= BMI < 34.9:
            result_text = "Obesity Class 1"
        elif 35 <= BMI < 39.9:
            result_text = "Obesity Class 2"
        else:
            result_text = "Extreme Obesity"

        # Update the label with the result
        result_label.config(text=f"BMI: {BMI:.2f}\n{result_text}")

    except ValueError:
        result_label.config(text="Please enter valid numbers")


# Button to calculate BMI
but = Button(text="Calculate", command=click_the_button)
but.pack(pady=20)

# Label to display the result below the button
result_label = Label(text="", font=("Times New Roman", 12, "normal"))
result_label.pack()


window.mainloop()
