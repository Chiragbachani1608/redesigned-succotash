import tkinter as tk
from tkinter import ttk
from plyer import notification
import webbrowser
import schedule
import threading
import time

class SkincareProduct:
    def __init__(self, name, brand, purpose, product_url):
        self.name = name
        self.brand = brand
        self.purpose = purpose
        self.product_url = product_url

class SkincareRoutine:
    def __init__(self, time, product):
        self.time = time
        self.product = product

# Example skincare products with provided URLs
cosrx_cleanser = SkincareProduct("Low pH Good Morning Gel Cleanser", "Cosrx", "Cleansing",
                                 "https://www.amazon.in/Cosrx-Good-Morning-Cleanser-150ml/dp/B01N6LU7L6/ref=sr_1_3?adgrpid=1322714093675113&dib=eyJ2IjoiMSJ9._Zhx-MEV8glqRbY90TawzNASn9W0M6cU3tyEZkxfFZ5tfWwhZjm87_Qm2j70Fy6qokjA5bKZZPEcqJRovNynrIijY1xn2hFt8UV1VkzPIE9S_KPKKgqU7VM2dPyhx8RxjISRG7fIgpJLGAYObeXUrayJxAA3mb4_kGmgb7yc8JVpQetKIDl6H34yr1AlckPrdDK2HWsOouuQq0zOP-dEZGijjcVTzCG0c2TYFq4PwDT041dFzifaPQRDiIuYvgBj9_K46BboqvG8IbBRcSWA1tYHUofFT3g1Epo4STGh7EA.YWOOIawe_LtS0WFszZb34IMqVhNew9thcqIaEGJF-ec&dib_tag=se&hvadid=82669889905380&hvbmt=be&hvdev=c&hvlocphy=155796&hvnetw=o&hvqmt=e&hvtargid=kwd-82670509334433%3Aloc-90&hydadcr=8358_2157278&keywords=cosrx+low+ph+good+morning+gel+cleanser&qid=1705837903&sr=8-3")

kaya_moisturizer = SkincareProduct("Hydra-Cleanse Makeup Remover", "Kaya Skin Clinic", "Moisturizing",
                                   "https://www.amazon.in/Kaya-Skin-Clinic-Cleanse-Remover/dp/B01FK7RI6Q")

ordinary_serum = SkincareProduct("Niacinamide 10% + Zinc 1%", "The Ordinary", "Serum",
                                 "https://theordinary.com/en-us/niacinamide-10-zinc-1-serum-100436.html")

derma_co_sunscreen = SkincareProduct("Oil-Free Sunscreen SPF 30", "Derma Co", "Sunscreen",
                                     "https://www.amazon.in/Derma-Co-Moisturizer-Hyaluronic-Multivitamins/dp/B0B39MLQYZ/ref=sr_1_1?adgrpid=1316117028205779&dib=eyJ2IjoiMSJ9.poOJ6LgTPTeCBJCT5GU6DNMY3NKNgONmhvkZNHAT-D-3hsI9zMup7N3yA3azAkfm9zAsWkAn0yWkaYsAis2nGc1mto3K9iwG79UyUVpyY1xgn0-BNM8LVrK_lf_Oo2bNW1NLX-75jPk2i6E1KD2bbHFCEJqaUP22Q6nQ9Ds2wDTRGTKZUm77acC5ynM7CHmYfbnfNppqdt7SjHwUUjZvrmNctuZvrPpIKHt_TYkIGxxRl7DgX9VyLNvTm5KSAImr1bVVPpf2E66--imxhb1cPWqFdMshAJbLEDs3OQqCd2g.G_nfwbnRlFIY1IyJKW54lGC_NaX0MwxG2j2e6zlXOeE&dib_tag=se&hvadid=82257585697862&hvbmt=bp&hvdev=c&hvlocphy=155796&hvnetw=o&hvqmt=p&hvtargid=kwd-82258194837844%3Aloc-90&hydadcr=22006_2354550&keywords=derma+co+oil+free&qid=1705838187&sr=8-1")

# Store products in a list or database
skincare_products = [cosrx_cleanser, kaya_moisturizer, ordinary_serum, derma_co_sunscreen]

# GUI setup
root = tk.Tk()
root.title("Skincare Reminder by Chirag")

# Dropdown for selecting skincare products
product_label = tk.Label(root, text="Select Skincare Product:")
product_options = [product.name for product in skincare_products]
product_dropdown = ttk.Combobox(root, values=product_options)

# Entry widget for time details
routine_time_label = tk.Label(root, text="Time (minutes after which to be reminded):")
routine_time_entry = tk.Entry(root)

# Button to add a new routine and schedule a reminder
add_button = tk.Button(root, text="Add Routine", command=lambda: add_routine(skincare_products[product_dropdown.current()]))

# Button to open product link in a web browser
open_browser_button = tk.Button(root, text="Open Product Link", command=lambda: open_product_link(skincare_products[product_dropdown.current()]))

# Function to add a new skincare routine
def add_routine(product):
    try:
        time_minutes = int(routine_time_entry.get())
        new_routine = SkincareRoutine(time_minutes, product)
        schedule.every(time_minutes).minutes.do(lambda: remind_skincare_routine(new_routine.product.name))
        show_notification("Routine Added", f"Skincare routine added for {new_routine.product.name}!")
    except ValueError:
        show_notification("Error", "Please enter a valid integer for time.")

# Function to open the product link in a web browser
def open_product_link(product):
    webbrowser.open(product.product_url)

# Function to remind about skincare routine
def remind_skincare_routine(product_name):
    show_notification("Skincare Reminder", f"It's time for your skincare routine with {product_name}!")

# Function to show a desktop notification
def show_notification(title, message):
    notification.notify(
        title=title,
        message=message,
        app_icon=None,
        timeout=10,
    )

# Function to display a healthy skincare routine in the GUI
def display_healthy_routine():
    healthy_routine_text = """
   Morning Routine:

Cleansing:

Start your day with the Cosrx Low pH Good Morning Gel Cleanser to gently cleanse your skin and remove any impurities accumulated overnight.
Toning:

After cleansing, apply a hydrating toner to balance your skin's pH and prepare it for the upcoming steps. Look for toners with ingredients that provide hydration and nourishment.
Serum:

Incorporate The Ordinary Niacinamide 10% + Zinc 1% serum into your morning routine. This serum targets specific skin concerns and provides concentrated ingredients to address them.
Moisturizing:

Apply a suitable moisturizer like the Derma Co Oil-Free Sunscreen SPF 30 to keep your skin hydrated and protected throughout the day. This step helps prevent dryness and maintains the skin's moisture balance.
Sunscreen:

Finish your morning routine with a broad-spectrum sunscreen to shield your skin from harmful UV rays. The Derma Co Oil-Free Sunscreen SPF 30 not only moisturizes but also provides essential sun protection.
Evening Routine:

Cleansing:

Use the Cosrx Low pH Good Morning Gel Cleanser again to cleanse your face and remove makeup, dirt, and pollutants accumulated during the day.
Toning:

Apply a hydrating toner in the evening to replenish your skin's moisture levels after cleansing.
Serum:

Before bedtime, incorporate The Ordinary Niacinamide 10% + Zinc 1% serum into your routine once more. This concentrated formula addresses specific skin concerns and promotes skin health overnight.
Moisturizing:

Use the Derma Co Oil-Free Sunscreen SPF 30 as your nighttime moisturizer. It helps keep your skin hydrated while avoiding excess oiliness.
Additional Tips:

Customization:

Customize your routine based on your skin type and specific needs. If you have additional concerns, consider incorporating targeted treatments or adjusting the frequency of certain products.
Consistency:

Consistency is crucial for achieving healthy and radiant skin. Stick to your daily routine to see long-term benefits. Adjustments can be made as needed, but avoid abrupt changes that may disrupt your skin's balance.
Extras:

Consider adding masks or treatments 1-2 times a week based on your skin's requirements. This could include exfoliation, hydrating masks, or any specialized treatments recommended for your skin concerns.
Remember to monitor your skin's response and make adjustments accordingly for optimal results.Consistency is key for achieving healthy and radiant skin!
    """
    # Display the healthy skincare routine in a new window
    healthy_routine_window = tk.Toplevel(root)
    healthy_routine_window.title("Healthy Skincare Routine")

    text_widget = tk.Text(healthy_routine_window, wrap="word", height=20, width=80)
    text_widget.insert(tk.END, healthy_routine_text)
    text_widget.config(state="disabled")
    text_widget.pack(padx=10, pady=10)

# Button to display the healthy skincare routine
display_healthy_button = tk.Button(root, text="Display Healthy Skincare Routine", command=display_healthy_routine)

# Pack widgets into the GUI
product_label.pack(pady=10)
product_dropdown.pack(pady=10)
routine_time_label.pack(pady=10)
routine_time_entry.pack(pady=10)
add_button.pack(pady=10)
open_browser_button.pack(pady=10)
display_healthy_button.pack(pady=10)
print("Made By Chirag")
# Run the GUI
root.mainloop()