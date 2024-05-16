from tkinter import *
from tkinter import ttk
from ttkthemes import ThemedTk
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Function to run the bot
def run_bot():
    url = url_entry.get()  # Get URL from the entry widget

    # Print the URL
    print(f"URL: {url}")

    # Initialize the Selenium WebDriver with the correct path to chromedriver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    # Open the URL with the WebDriver
    driver.get(url)

# Create the main window with a theme
root = ThemedTk(theme="radiance")
root.title("Web Scraping Bot Interface")

# Load the background image
background_image = PhotoImage(file="background_image1.jpg")

# Set the background image
background_label = Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Create a ThemedStyle object
style = ttk.Style()

# Create a custom style for Label widget
style.configure("TLabel", foreground="blue", background="yellow")

# Apply the custom style to the Label widget
ttk.Label(root, text="Enter URL:", style="TLabel").grid(row=0, column=0, padx=10, pady=10)

# Create a custom style for Entry widget
style.configure("TEntry", foreground="white", background="black")

# Apply the custom style to the Entry widget
url_entry = ttk.Entry(root, width=50, style="TEntry")
url_entry.grid(row=0, column=1, padx=10, pady=10)

# Create a custom style for Button widget
style.configure("TButton", foreground="white", background="green")

# Create a button to run the bot using ttk widgets
ttk.Button(root, text="Run Bot", command=run_bot, style="TButton").grid(row=1, column=0, columnspan=2, pady=10)

# Run the main event loop
root.mainloop()
