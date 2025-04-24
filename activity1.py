class Smartphone:
    """
    A class representing a basic smartphone.
    """
    def __init__(self, brand, model, imei, display_size, storage_capacity, battery_capacity):
        """
        Constructor to initialize a Smartphone object.

        Args:
            brand (str): The brand of the smartphone.
            model (str): The model name of the smartphone.
            imei (str): The unique International Mobile Equipment Identity number.
            display_size (float): The size of the display in inches.
            storage_capacity (int): The storage capacity in GB.
            battery_capacity (int): The battery capacity in mAh.
        """
        self.brand = brand
        self.model = model
        self.imei = imei
        self.display_size = display_size
        self.storage_capacity = storage_capacity
        self.battery_capacity = battery_capacity
        self.is_on = False
        self.apps_installed = []
        print(f"{self.brand} {self.model} with IMEI {self.imei} created.")

    def power_on(self):
        """
        Turns the smartphone on.
        """
        if not self.is_on:
            self.is_on = True
            print(f"{self.brand} {self.model} is powering on...")
        else:
            print(f"{self.brand} {self.model} is already on.")

    def power_off(self):
        """
        Turns the smartphone off.
        """
        if self.is_on:
            self.is_on = False
            print(f"{self.brand} {self.model} is powering off.")
        else:
            print(f"{self.brand} {self.model} is already off.")

    def install_app(self, app_name):
        """
        Installs a new app on the smartphone.

        Args:
            app_name (str): The name of the app to install.
        """
        if app_name not in self.apps_installed:
            self.apps_installed.append(app_name)
            print(f"{app_name} installed on {self.brand} {self.model}.")
        else:
            print(f"{app_name} is already installed on {self.brand} {self.model}.")

    def uninstall_app(self, app_name):
        """
        Uninstalls an app from the smartphone.

        Args:
            app_name (str): The name of the app to uninstall.
        """
        if app_name in self.apps_installed:
            self.apps_installed.remove(app_name)
            print(f"{app_name} uninstalled from {self.brand} {self.model}.")
        else:
            print(f"{app_name} is not installed on {self.brand} {self.model}.")

    def list_apps(self):
        """
        Lists all the installed apps on the smartphone.
        """
        if self.apps_installed:
            print(f"Installed apps on {self.brand} {self.model}: {', '.join(self.apps_installed)}")
        else:
            print(f"No apps installed on {self.brand} {self.model} yet.")

    def display_info(self):
        """
        Displays the basic information about the smartphone.
        """
        print(f"\n--- {self.brand} {self.model} Info ---")
        print(f"IMEI: {self.imei}")
        print(f"Display Size: {self.display_size} inches")
        print(f"Storage Capacity: {self.storage_capacity} GB")
        print(f"Battery Capacity: {self.battery_capacity} mAh")
        print(f"Status: {'On' if self.is_on else 'Off'}")
        self.list_apps()
        print("--- End of Info ---")

    def take_photo(self):
        """
        Simulates taking a basic photo with the smartphone.
        """
        if self.is_on:
            print(f"{self.brand} {self.model} captures a photo.")
        else:
            print(f"Please power on {self.brand} {self.model} to take a photo.")

# Inheritance Layer: Creating a more specialized type of Smartphone
class CameraSmartphone(Smartphone):
    """
    A class representing a smartphone with advanced camera features,
    inheriting from the Smartphone class.
    """
    def __init__(self, brand, model, imei, display_size, storage_capacity, battery_capacity,
                 megapixel_count, has_optical_zoom):
        """
        Constructor for CameraSmartphone, inheriting from Smartphone and adding camera features.

        Args:
            brand (str): The brand of the smartphone.
            model (str): The model name of the smartphone.
            imei (str): The unique IMEI number.
            display_size (float): The size of the display in inches.
            storage_capacity (int): The storage capacity in GB.
            battery_capacity (int): The battery capacity in mAh.
            megapixel_count (int): The megapixel count of the main camera.
            has_optical_zoom (bool): Indicates if the camera has optical zoom.
        """
        super().__init__(brand, model, imei, display_size, storage_capacity, battery_capacity)
        self.megapixel_count = megapixel_count
        self.has_optical_zoom = has_optical_zoom
        print(f"{self.brand} {self.model} (Camera Edition) created with a {self.megapixel_count}MP camera.")

    def take_photo(self):
        """
        Simulates taking a high-quality photo with the advanced camera.
        """
        if self.is_on:
            print(f"{self.brand} {self.model}'s {self.megapixel_count}MP camera captures a stunning photo!")
        else:
            print(f"Please power on {self.brand} {self.model} to take a photo.")

    def record_video(self, duration_seconds):
        """
        Simulates recording a video with advanced features.

        Args:
            duration_seconds (int): The duration of the video in seconds.
        """
        if self.is_on:
            print(f"{self.brand} {self.model} is recording a high-resolution {duration_seconds} second video.")
        else:
            print(f"Please power on {self.brand} {self.model} to record a video.")

    # Polymorphism: Overriding a method from the parent class
    def display_info(self):
        """
        Overrides the display_info method to include camera specific information.
        """
        super().display_info()
        print(f"\n--- Camera Features ---")
        print(f"Megapixel Count: {self.megapixel_count} MP")
        print(f"Optical Zoom: {'Yes' if self.has_optical_zoom else 'No'}")
        print("--- End of Camera Info ---")

# Creating instances of the classes
phone1 = Smartphone("Samsung", "Galaxy S23", "358765432109876", 6.1, 128, 3900)
phone2 = Smartphone("Apple", "iPhone 15", "012345678901234", 6.1, 256, 3877)
camera_phone = CameraSmartphone("Google", "Pixel 8 Pro", "987654321012345", 6.7, 256, 5050, 50, True)

# Using the methods
phone1.power_on()
phone1.install_app("WhatsApp")
phone1.install_app("Instagram")
phone1.list_apps()
phone1.take_photo() # Now this will call the take_photo method in the base Smartphone class
phone1.power_off()
phone1.display_info()

print("\n--- Camera Phone Actions ---")
camera_phone.power_on()
camera_phone.install_app("Snapseed")
camera_phone.list_apps()
camera_phone.take_photo() # This will call the take_photo method in the CameraSmartphone class
camera_phone.record_video(60)
camera_phone.display_info()
camera_phone.power_off()

print("\n--- Another Phone ---")
phone2.power_on()
phone2.install_app("Telegram")
phone2.display_info()
phone2.power_off()