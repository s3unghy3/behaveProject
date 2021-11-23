import os


def banner():
    os.system("behave features/banner.feature")


def contact_us():
    os.system("behave features/contact_us.feature")


def empty_cart():
    os.system("behave features/empty_cart.feature")


def order_steps():
    os.system("behave features/order_steps.feature")


def search():
    os.system("behave features/search.feature")


def sign_in():
    os.system("behave features/sign_in.feature")


def sign_up():
    os.system("behave features/sign_up.feature")


def social_media():
    os.system("behave features/social_media.feature")


def main():
    pass


if __name__ == "__main__":
    banner()
    contact_us()
    empty_cart()
    order_steps()
    search()
    sign_in()
    sign_up()
    social_media()