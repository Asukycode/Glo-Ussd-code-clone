print("~~Rule Your world Glo~~")
print("Welcome to Glo Customer Care Service enter ussd code below")


def proceed_data(data_amt_validity: str):
    tel = input("\t\t\tPlease enter phone number: ")
    if len(tel) == 11 and tel[0] == "0" and tel.isnumeric():
        print(f'\t\t\t{tel} just received {data_amt_validity}')
    else:
        print("Invalid phone number")


def data_section():
    entry = int(input(
        '''
    1. Mini Plans
    2. Monthly Plans
    3. Mega Plans
    4. Super Mega Plans
    5. Special Data Offer
    6. Social Bundles
    7. Night and Weekend Plans

    select transaction
    '''))
    if entry == 1:
        mini_plans = {
            "N100": "150 MB 1 Day incl 35MB nite",
            "N200": "350 MB 2 Days incl 110MB nite",
            "N500": "1.8 GB 14 Days incl 1GB nite",
            "N50": "50 MB 1 Day incl 5MB nite",

        }
        count = 0
        for k, v in mini_plans.items():
            count += 1
            print(f'\t\t\t\t{count}. {k} = {v}')
        entry = int(input("\t\t\tSelect transaction: "))
        if entry == 1:
            proceed_data(mini_plans.get("N100"))
        elif entry == 2:
            proceed_data(mini_plans.get("N200"))
        elif entry == 3:
            proceed_data(mini_plans.get("N500"))
        elif entry == 4:
            proceed_data(mini_plans.get("N50"))
        else:
            print("invalid")

    elif entry == 2:
        monthly_plans = {
            "N1000": "3.9GB 30Days incl 1GB nite",
            "N1500": "7.5GB 30Days incl 4GB nite",
            "N2000": "9.2GB 30Days incl 4GB nite",
            "N2500": "10.8GB 30Days incl 4GB nite",

        }
        count = 0
        for k, v in monthly_plans.items():
            count += 1
            print(f'\t\t\t\t{count}. {k} = {v}')

        entry = int(input("\t\t\tSelect transaction: "))
        if entry == 1:
            proceed_data(monthly_plans.get("N1000"))
        elif entry == 2:
            proceed_data(monthly_plans.get("N1500"))
        elif entry == 3:
            proceed_data(monthly_plans.get("N2000"))
        elif entry == 4:
            proceed_data(monthly_plans.get("N2500"))
        else:
            print("invalid")

    elif entry == 3:
        mega_plans = {
            "N10000": "50GB 30Days incl 4GB nite",
            "N15000": "93GB 30Days incl 7GB nite",
            "N18000": "119GB 30Days incl 10GB nite",
            "N20000": "138GB 30Days incl 12GB nite",

        }
        count = 0
        for k, v in mega_plans.items():
            count += 1
            print(f'\t\t\t\t{count}. {k} = {v}')
        entry = int(input("\t\t\tSelect transaction: "))
        if entry == 1:
            proceed_data(mega_plans.get("N1000"))
        elif entry == 2:
            proceed_data(mega_plans.get("N1500"))
        elif entry == 3:
            proceed_data(mega_plans.get("N2000"))
        elif entry == 4:
            proceed_data(mega_plans.get("N2500"))
        else:
            print("invalid")

    elif entry == 4:
        super_mega_plans = {
            "N30000": "225GB 30 Days",
            "N36000": "300GB 30 Days",
            "N50000": "425GB 90 Days",
            "N60000": "525GB 120Days",
            "N75000": "675GB 120 days",
            "N100000": "1024 GB 1 year"

        }
        count = 0
        for k, v in super_mega_plans.items():
            count += 1
            print(f'\t\t\t\t{count}. {k} = {v}')
        entry = int(input("\t\t\tSelect transaction: "))
        if entry == 1:
            proceed_data(super_mega_plans.get("N30000"))
        elif entry == 2:
            proceed_data(super_mega_plans.get("N36000"))
        elif entry == 3:
            proceed_data(super_mega_plans.get("N50000"))
        elif entry == 4:
            proceed_data(super_mega_plans.get("N60000"))
        elif entry == 5:
            proceed_data(super_mega_plans.get("N75000"))
        elif entry == 6:
            proceed_data(super_mega_plans.get("N100000"))
        else:
            print("invalid")


    elif entry == 5:
        special_data_offer = int(input(
            '''
            1. Special Plans
            2. Campus Booster
            3. Badagry Plans
            4. Data Booster
            0. Exit
            '''
        ))

    elif entry == 6:
        social_bundles = int(input(
            '''
            1. WTF (Whatsapp, Twitter and Facebook) Bundles
            2. Youtube Bundles 
            3. Opera Bundles
            4. Single Bundles
            '''
        ))


    elif entry == 7:
        night_and_weekend_plans = {
            "N25": "250MB 1Day (12am-05am)",
            "N50": "500MB 1Day (12am-05am)",
            "N100": "1GB 5Days (12am-05am)",
            "N200": "1.25GB 1Day SUN",
            "N500": "3GB 2Days SAT-SUN"
        }

        count = 0
        for k, v in night_and_weekend_plans.items():
            count += 1
            print(f'\t\t\t\t{count}. {k} = {v}')
        entry = int(input("\t\t\tSelect transaction: "))
        if entry == 1:
            proceed_data(night_and_weekend_plans.get("N25"))
        elif entry == 2:
            proceed_data(night_and_weekend_plans.get("N50"))
        elif entry == 3:
            proceed_data(night_and_weekend_plans.get("N100"))
        elif entry == 4:
            proceed_data(night_and_weekend_plans.get("N200"))
        elif entry == 5:
            proceed_data(night_and_weekend_plans.get("N500"))
        else:
            print("invalid")
    elif entry == 0:
        pass


def data_share():
    entry = int(input('''
                    Share data plan

                    1. Share 
                    2. Unshare
                    '''))
    if entry == 1:
        tel = input("Please enter subscriber's number: ")
        if len(tel) == 11 and tel[0] == "0" and tel.isnumeric():
            print(f'\t\t\tYou just shared your data with {tel}')
    elif entry == 2:
        tel = input("Please enter subscriber's number: ")
        if len(tel) == 11 and tel[0] == "0" and tel.isnumeric():
            print(f'\t\t\tYou just unshared your data with {tel}')


def e_top_up():
    entry = int(input("""
        Welcome to Glo e-Services
        Please select an option
        
        1. Airtime
        2. Data
    """))
    if entry == 1:
        entry = int(input("""
        Please select type of Airtime
        
        1. 5X Recharges
        2. Regular Recharges
        0. Exit
        """))
        if entry == 1:
            entry = int(input("""
            1. Self
            2. Third party
            """))
            if entry == 1:
                entry = int(input("""
                Select 5X amount
                1. N120
                2. N220
                3. N320
                4. N420
                5. N520
                6. N620
                7. N720
                """))
                offers = ["N120", "N220", "N320", "N420", "N520", "N620", "N720"]
                if entry == 1:
                    print(f'You have been credited with a 5X Recharge of {offers[0]}')
                elif entry == 2:
                    print(f'You have been credited with a 5X Recharge of {offers[1]}')
                elif entry == 3:
                    print(f'You have been credited with a 5X Recharge of {offers[2]}')
                elif entry == 4:
                    print(f'You have been credited with a 5X Recharge of {offers[3]}')
                elif entry == 5:
                    print(f'You have been credited with a 5X Recharge of {offers[4]}')
                elif entry == 6:
                    print(f'You have been credited with a 5X Recharge of {offers[5]}')
                elif entry == 7:
                    print(f'You have been credited with a 5X Recharge of {offers[6]}')
            elif entry == 2:
                tel = input("Please enter Third party number: ")
                if len(tel) == 11 and tel[0] == "0" and tel.isnumeric():
                    entry = int(input("""
                                    Select 5X amount
                                    1. N120
                                    2. N220
                                    3. N320
                                    4. N420
                                    5. N520
                                    6. N620
                                    7. N720
                                    """))
                    offers = ["N120", "N220", "N320", "N420", "N520", "N620", "N720"]
                    if entry == 1:
                        print(f'You have been credited {tel} with a 5X Recharge of {offers[0]}')
                    elif entry == 2:
                        print(f'You have been credited {tel} with a 5X Recharge of {offers[1]}')
                    elif entry == 3:
                        print(f'You have been credited {tel} with a 5X Recharge of {offers[2]}')
                    elif entry == 4:
                        print(f'You have been credited {tel} with a 5X Recharge of {offers[3]}')
                    elif entry == 5:
                        print(f'You have been credited {tel} with a 5X Recharge of {offers[4]}')
                    elif entry == 6:
                        print(f'You have been credited {tel} with a 5X Recharge of {offers[5]}')
                    elif entry == 7:
                        print(f'You have been credited {tel} with a 5X Recharge of {offers[6]}')
        elif entry == 2:
            entry = int(input("""
                        1. Self
                        2. Third party
                        """))
            if entry == 1:
                amt = int(input("Please Enter Amount"))
                if amt > 0:
                    print(f"You have been credited with {amt} of Airtime")
            if entry == 2:
                tel = input("Please enter Third party number: ")
                if len(tel) == 11 and tel[0] == "0" and tel.isnumeric():
                    amt = int(input("Please Enter Amount"))
                    if amt > 0:
                        print(f"You have credited {tel} with {amt} of Airtime")
    elif entry == 2:
        entry = int(input('''
        Data Plan Purchase
        
        1. Self
        2. Third party
        '''))
        if entry == 1:
            entry = int(input('''
            Oga sim gets additional Bonus
            
            1. N100 = 105MB 1Day incl 15MB nite
            2. N200 = 350MB 2Days incl 110MB nite
            3. N500 = 1.05GB 14Days incl 250MB nite
            4. N1000 = 2.5GB 30Days incl 600MB nite
            '''))
            if entry == 1:
                print("You have been credited with 105MB 1Day incl 15MB nite")
            elif entry == 2:
                print("You have been credited with 350MB 2Days incl 110MB nite")
            elif entry == 3:
                print("You have been credited with 1.05GB 14Days incl 250MB nite")
            elif entry == 4:
                print("You have been credited with 2.5GB 30Days incl 600MB nite")
        elif entry == 2:
            tel = input("Please enter Third party number: ")
            if len(tel) == 11 and tel[0] == "0" and tel.isnumeric():
                entry = int(input('''
                            Oga sim gets additional Bonus

                            1. N100 = 105MB 1Day incl 15MB nite
                            2. N200 = 350MB 2Days incl 110MB nite
                            3. N500 = 1.05GB 14Days incl 250MB nite
                            4. N1000 = 2.5GB 30Days incl 600MB nite
                            '''))
                if entry == 1:
                    print(f"You have credited {tel} with 105MB 1Day incl 15MB nite")
                elif entry == 2:
                    print(f"You have credited {tel} with 350MB 2Days incl 110MB nite")
                elif entry == 3:
                    print(f"You have credited {tel} with 1.05GB 14Days incl 250MB nite")
                elif entry == 4:
                    print(f"You have credited {tel} with 2.5GB 30Days incl 600MB nite")


def tarrif_plan():
    entry = int(input("""
                1. My Package\n
                2. Check Balance\n
                3. My Number\n
                4. Friends & Family\n
                5. Recharge\n
                6. Other Plans\n
                7. Voice Offers\n
                8. Exit
                """))
    if entry == 1:
        print("This Offer is available only for Glo Prepaid Customer")
    elif entry == 2:
        entry = int(input("""
            1. Main Balance
            2. Promo Account 1
            3. Promo Account 2
        """))
        if entry == 1:
            print("Your main account balance is ********")
        elif entry == 2:
            print("Your Promo Account 1 balance is ********")
        elif entry == 3:
            print("Your Promo Account 2 balance is ********")
    elif entry == 3:
        print("09163384323")
    elif entry == 4:
        entry = int(input("""
        1. Manage Friends and Family
        2. View Friends and Family
        
        """))
    elif entry == 5:
        entry = int(input("""
                Welcome to Glo e-Services
                Please select an option

                1. Airtime
                2. Data
            """))
        if entry == 1:
            entry = int(input("""
                Please select type of Airtime

                1. 5X Recharges
                2. Regular Recharges
                0. Exit
                """))
            if entry == 1:
                entry = int(input("""
                    1. Self
                    2. Third party
                    """))
                if entry == 1:
                    entry = int(input("""
                        Select 5X amount
                        1. N120
                        2. N220
                        3. N320
                        4. N420
                        5. N520
                        6. N620
                        7. N720
                        """))
                    offers = ["N120", "N220", "N320", "N420", "N520", "N620", "N720"]
                    if entry == 1:
                        print(f'You have been credited with a 5X Recharge of {offers[0]}')
                    elif entry == 2:
                        print(f'You have been credited with a 5X Recharge of {offers[1]}')
                    elif entry == 3:
                        print(f'You have been credited with a 5X Recharge of {offers[2]}')
                    elif entry == 4:
                        print(f'You have been credited with a 5X Recharge of {offers[3]}')
                    elif entry == 5:
                        print(f'You have been credited with a 5X Recharge of {offers[4]}')
                    elif entry == 6:
                        print(f'You have been credited with a 5X Recharge of {offers[5]}')
                    elif entry == 7:
                        print(f'You have been credited with a 5X Recharge of {offers[6]}')
                elif entry == 2:
                    tel = input("Please enter Third party number: ")
                    if len(tel) == 11 and tel[0] == "0" and tel.isnumeric():
                        entry = int(input("""
                                            Select 5X amount
                                            1. N120
                                            2. N220
                                            3. N320
                                            4. N420
                                            5. N520
                                            6. N620
                                            7. N720
                                            """))
                        offers = ["N120", "N220", "N320", "N420", "N520", "N620", "N720"]
                        if entry == 1:
                            print(f'You have been credited {tel} with a 5X Recharge of {offers[0]}')
                        elif entry == 2:
                            print(f'You have been credited {tel} with a 5X Recharge of {offers[1]}')
                        elif entry == 3:
                            print(f'You have been credited {tel} with a 5X Recharge of {offers[2]}')
                        elif entry == 4:
                            print(f'You have been credited {tel} with a 5X Recharge of {offers[3]}')
                        elif entry == 5:
                            print(f'You have been credited {tel} with a 5X Recharge of {offers[4]}')
                        elif entry == 6:
                            print(f'You have been credited {tel} with a 5X Recharge of {offers[5]}')
                        elif entry == 7:
                            print(f'You have been credited {tel} with a 5X Recharge of {offers[6]}')
            elif entry == 2:
                entry = int(input("""
                                1. Self
                                2. Third party
                                """))
                if entry == 1:
                    amt = int(input("Please Enter Amount"))
                    if amt > 0:
                        print(f"You have been credited with {amt} of Airtime")
                if entry == 2:
                    tel = input("Please enter Third party number: ")
                    if len(tel) == 11 and tel[0] == "0" and tel.isnumeric():
                        amt = int(input("Please Enter Amount"))
                        if amt > 0:
                            print(f"You have credited {tel} with {amt} of Airtime")
        elif entry == 2:
            entry = int(input('''
                Data Plan Purchase

                1. Self
                2. Third party
                '''))
            if entry == 1:
                entry = int(input('''
                    Oga sim gets additional Bonus

                    1. N100 = 105MB 1Day incl 15MB nite
                    2. N200 = 350MB 2Days incl 110MB nite
                    3. N500 = 1.05GB 14Days incl 250MB nite
                    4. N1000 = 2.5GB 30Days incl 600MB nite
                    '''))
                if entry == 1:
                    print("You have been credited with 105MB 1Day incl 15MB nite")
                elif entry == 2:
                    print("You have been credited with 350MB 2Days incl 110MB nite")
                elif entry == 3:
                    print("You have been credited with 1.05GB 14Days incl 250MB nite")
                elif entry == 4:
                    print("You have been credited with 2.5GB 30Days incl 600MB nite")
            elif entry == 2:
                tel = input("Please enter Third party number: ")
                if len(tel) == 11 and tel[0] == "0" and tel.isnumeric():
                    entry = int(input('''
                                    Oga sim gets additional Bonus

                                    1. N100 = 105MB 1Day incl 15MB nite
                                    2. N200 = 350MB 2Days incl 110MB nite
                                    3. N500 = 1.05GB 14Days incl 250MB nite
                                    4. N1000 = 2.5GB 30Days incl 600MB nite
                                    '''))
                    if entry == 1:
                        print(f"You have credited {tel} with 105MB 1Day incl 15MB nite")
                    elif entry == 2:
                        print(f"You have credited {tel} with 350MB 2Days incl 110MB nite")
                    elif entry == 3:
                        print(f"You have credited {tel} with 1.05GB 14Days incl 250MB nite")
                    elif entry == 4:
                        print(f"You have credited {tel} with 2.5GB 30Days incl 600MB nite")

def GLOTV():
    entry = int(input("""
                1. Proceed(Auto-Renew)
                2. Proceed (One-off)
                0. Back
                """))
    if entry == 1:

        entry = int(input('''
        1. N150 = VOD 500mb 3days
        2. N450 = VOD 2gb 7days
        3. N1400 = VOD 6gb 30 days
        4. N900 = VOD +TV 2gb 7days
        5. N3200 = VOD+TV 6gb 30days
        '''))
        if entry ==1:
            print(f'You just subscribed for GLOTV  ')
            print("And have been credited with VOD 500mb 3days")
        elif entry == 2:
            print(f'You just subscribed for GLOTV  ')
            print("And have been credited with VOD 2gb 7days")
        elif entry == 3:
            print(f'You just subscribed for GLOTV  ')
            print("And have been credited with VOD 6gb 30 days")
        elif entry == 4:
            print(f'You just subscribed for GLOTV  ')
            print("And have been credited with VOD +TV 2gb 7days")
        elif entry == 5:
            print(f'You just subscribed for GLOTV  ')
            print("And have been credited with VOD+TV 6gb 30days")

    if entry == 2:
        entry = int(input('''
        1. N150 = VOD 500mb 3days
        2. N450 = VOD 2gb 7days
        3. N1400 = VOD 6gb 30 days
        4. N900 = VOD +TV 2gb 7days
        5. N3200 = VOD+TV 6gb 30days
        '''))
        if entry ==1:
            print(f'You just subscribed for GLOTV  ')
            print("And have been credited with VOD 500mb 3days")
        elif entry == 2:
            print(f'You just subscribed for GLOTV  ')
            print("And have been credited with VOD 2gb 7days")
        elif entry == 3:
            print(f'You just subscribed for GLOTV  ')
            print("And have been credited with VOD 6gb 30 days")
        elif entry == 4:
            print(f'You just subscribed for GLOTV  ')
            print("And have been credited with VOD +TV 2gb 7days")
        elif entry == 5:
            print(f'You just subscribed for GLOTV  ')
            print("And have been credited with VOD+TV 6gb 30days")

def VAS():

while True:
    user_ussd = input(
        '''
        Enter ussd code :
        '''
    )
    if user_ussd == "*777#":
        user_entry = int(input(
            """
            1. Data 
            2. Borrow Credit or Data 
            3. E-Top Up
            4. Berekete 10X
            5. My Tariff Plan 
            6. Intl Calls & Roaming 
            7. GLOTV
            8. 11KOBO Plan
            9. VAS
            0. Exit
            
           Select Transaction:  
            """
        ))
        if user_entry == 1:
            user_entry_1 = int(input('''
            DATA
            1. Buy Data Plan 
            2. Match Day Special Offer 
            3. Show max Data offer 
            4. Gift Data Plan 
            5. Share Data Plan
            6. Check Data Balance 
            7. Manage Data Plan
            8. Blackberry 
            0. Back
            
            Select Transaction 
            '''))
            if user_entry_1 == 1:
                entry = int(input('''
                1. Proceed (Auto-Renew)\n
                2. Proceed (0ne-off)
                
                select transaction
                '''))
                if entry == 1:
                    data_section()

                elif entry == 2:
                    data_section()
            elif user_entry_1 == 2:
                print(f'\t\t\t\tError communicating with ESME')
            elif user_entry_1 == 3:
                entry = int(input('''
                Please select 
                1. Showmax Mobile Only Access-N1200, 30days
                2. Showmax Mobile -N1400, 1.5GB, 30days
                3. Showmax Mobile -N1700, 3GB, 30days
                '''))
                if entry == 1 or 2 or 3:
                    print("Thank you for subscribing to showmax pack. You will \n recieve the link to register for "
                          "showmax service")
            elif user_entry_1 == 4:
                print("Gift data plans")
                data_section()
            elif user_entry_1 == 5:
                print("share data plans")
                data_share()
            elif user_entry_1 == 6:
                print("Check Data balance")
                print(f'''
                Dear customer, your plan has expired and you do not have a data plan.
                To buy a data plan and continue browsing visit http://hsi.glo.com or dial *777#
                ''')
            elif user_entry_1 == 7:
                print("""
                1. To get Data Settings
                2. To See Details For manual
                3. To go to selfcare Portal
                4. Get Data Balance
                5. To Check Sharing Members
                """)
            elif user_entry_1 == 8:
                print("""
                All Glo BB10 data Plans are
                now 3G-4G compatible
                1. Buy 3G-4G BB data
                2. Manage
                0. Exit
                """)




        elif user_entry == 2:
            print('''            ------------------------------------------------------
            Dear Customer, to qualify for this 
            service, you should\n\t\t\thave been on the Glo network for 3 months with N200\n\t\t\tmonthly 
            usage.\n\t\t\t------------------------------------------------------''')
        elif user_entry == 3:
            e_top_up()
        elif user_entry == 4:
            user_entry_4 = int(
                input('''

                      Enjoy 700% bonus to call all networks + FREE Data\n\t\t\ton every recharge\n

                      1. Migrate Now 
                      2. Back
                      3. Exit
                      ''')
            )
            if user_entry_4 == 1:
                print('''
                Dear customer, you are now on GLo Brekete 10X. Recharge
                N100 and Make a call to get N1000 sign-on bonus. Also
                enjoy 10X bonus on all recharges for calls and data. 
                ''')
        elif user_entry == 5:
            tarrif_plan()
        elif user_entry == 6:
            user_entry_6 = int(input("""
            1. Int'l Call Offers\n
            2. Data Roaming Bundles\n
            0. Exit
            """))
            if user_entry_6 == 1:
                entry = int(input('''
                1. N100 = 9Min 3Days
                2. N200 = 19Min 7Days
                3. N500 = 43 Min 14Days
                4. N1000 = 93 Min 30days
                '''))
                if entry == 1:
                    print("You have been Credited with N100")
                elif entry == 2:
                    print("You have been Credited with N200")
                elif entry == 3:
                    print("You have been Credited with N500")
                elif entry == 4:
                    print("You have been Credited with N1000")
            elif user_entry_6 == 2:
                data_section()
        elif user_entry == 7:
            GLOTV()
        elif user_entry == 8:
            user_entry_8 = int(input(
                '''
                The most affordable 11k/sec Tariff Plan.
                press:
                
                1. To subscribe
                2. Back
                Alternatively dial *311# to subscribe
                '''
            ))
            if user_entry_8 == 1:
                print("welcome to GLO_11KOBO_PLAN")

        elif user_entry == 9:
            user_entry_9 = int(input('''
            1. Game box
            2. GLo Cloud
            3. Busuu Language learning 
            4. Gaming Protal
            5. Caller Tunes
            6. Borrow Me Credit
            7. Unsubscribe
            0. Exit
            
            '''))
    else:
        print("Wrong ussd code 🥲")
        print("Try again !")
        continue
