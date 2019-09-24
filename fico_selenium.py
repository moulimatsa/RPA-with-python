import pyautogui
import pyperclip
import numpy as np
import random
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0

url = "https://www.myfico.com/fico-credit-score-estimator/estimator"

# create a new Firefox session
driver = webdriver.Chrome()
driver.implicitly_wait(30)
driver.get(url)


def score(i):
    print(dataset['sk_id_curr'][i])
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//span[@id='estimated-score']")))
    #element = driver.find_element_by_xpath("//span[@id='estimated-score']")
    elementText = element.text
    # pyautogui.click(809,747)
    # score_1 = pyperclip.paste()
    fo = open("modified.txt", 'a+')
    fo.write(str(dataset['sk_id_curr'][i]) + "-" + str(elementText) + "\n")

    # pyautogui.typewrite(dataset['sk_id_curr'][i])
    # pyautogui.hotkey('ctrl', 'v')
    # pyautogui.click(660,747)


def q1_2(i):
    if dataset['first_cc'][i] < 0.5:
        python_button = driver.find_element_by_xpath("//button[@data-answer='1a_a'] ")
        python_button.click()
        q2(i)


    elif dataset['first_cc'][i] >= 0.5 and dataset['first_cc'][i] < 2:
        python_button = driver.find_element_by_xpath("//button[@data-answer='1a_b'] ")
        python_button.click()
        q2a(i)


    elif dataset['first_cc'][i] >= 2 and dataset['first_cc'][i] < 4:
        python_button = driver.find_element_by_xpath("//button[@data-answer='1a_c'] ")
        python_button.click()
        q2a(i)

    elif dataset['first_cc'][i] >= 4 and dataset['first_cc'][i] < 5:
        python_button = driver.find_element_by_xpath("//button[@data-answer='1a_d'] ")
        python_button.click()
        q2a(i)

    elif dataset['first_cc'][i] >= 5 and dataset['first_cc'][i] < 8:
        python_button = driver.find_element_by_xpath("//button[@data-answer='1a_e'] ")
        python_button.click()
        q2a(i)

    elif dataset['first_cc'][i] >= 8 and dataset['first_cc'][i] < 10:
        python_button = driver.find_element_by_xpath("//button[@data-answer='1a_f'] ")
        python_button.click()
        q2a(i)

    elif dataset['first_cc'][i] >= 10 and dataset['first_cc'][i] < 15:
        python_button = driver.find_element_by_xpath("//button[@data-answer='1a_g'] ")
        python_button.click()
        q2a(i)

    elif dataset['first_cc'][i] >= 15 and dataset['first_cc'][i] < 20:
        python_button = driver.find_element_by_xpath("//button[@data-answer='1a_h'] ")
        python_button.click()
        q2a(i)

    elif dataset['first_cc'][i] >= 20:
        python_button = driver.find_element_by_xpath("//button[@data-answer='1a_i'] ")
        python_button.click()
        q2a(i)

    else:
        print("I have failed you sensei!")


def q2(i):
    if dataset['first_loan'][i] == 0:
        python_button = driver.find_element_by_xpath("//button[@data-answer='2_a'] ")
        python_button.click()

    elif 0 < dataset['first_loan'][i] < 0.5:
        python_button = driver.find_element_by_xpath("//button[@data-answer='2_b'] ")
        python_button.click()

    elif dataset['first_loan'][i] >= 0.5 and dataset['first_loan'][i] < 2:
        python_button = driver.find_element_by_xpath("//button[@data-answer='2_c'] ")
        python_button.click()

    elif dataset['first_loan'][i] >= 2 and dataset['first_loan'][i] < 5:
        python_button = driver.find_element_by_xpath("//button[@data-answer='2_d'] ")
        python_button.click()

    elif dataset['first_loan'][i] >= 5 and dataset['first_loan'][i] < 10:
        python_button = driver.find_element_by_xpath("//button[@data-answer='2_e'] ")
        python_button.click()

    elif dataset['first_loan'][i] >= 10 and dataset['first_loan'][i] < 15:
        python_button = driver.find_element_by_xpath("//button[@data-answer='2_f'] ")
        python_button.click()

    elif dataset['first_loan'][i] >= 15 and dataset['first_loan'][i] < 20:
        python_button = driver.find_element_by_xpath("//button[@data-answer='2_g'] ")
        python_button.click()

    elif dataset['first_loan'][i] >= 20:
        python_button = driver.find_element_by_xpath("//button[@data-answer='2_h'] ")
        python_button.click()

    else:
        print("I have failed you sensei!")


def q2a(i):
    if dataset['first_loan'][i] == 0:
        python_button = driver.find_element_by_xpath("//button[@data-answer='2a_a'] ")
        python_button.click()

    elif 0 < dataset['first_loan'][i] < 0.5:
        python_button = driver.find_element_by_xpath("//button[@data-answer='2a_b'] ")
        python_button.click()

    elif dataset['first_loan'][i] >= 0.5 and dataset['first_loan'][i] < 2:
        python_button = driver.find_element_by_xpath("//button[@data-answer='2a_c'] ")
        python_button.click()

    elif dataset['first_loan'][i] >= 2 and dataset['first_loan'][i] < 5:
        python_button = driver.find_element_by_xpath("//button[@data-answer='2a_d'] ")
        python_button.click()

    elif dataset['first_loan'][i] >= 5 and dataset['first_loan'][i] < 10:
        python_button = driver.find_element_by_xpath("//button[@data-answer='2a_e'] ")
        python_button.click()

    elif dataset['first_loan'][i] >= 10 and dataset['first_loan'][i] < 15:
        python_button = driver.find_element_by_xpath("//button[@data-answer='2a_f'] ")
        python_button.click()

    elif dataset['first_loan'][i] >= 15 and dataset['first_loan'][i] < 20:
        python_button = driver.find_element_by_xpath("//button[@data-answer='2a_g'] ")
        python_button.click()

    elif dataset['first_loan'][i] >= 20:
        python_button = driver.find_element_by_xpath("//button[@data-answer='2a_h'] ")
        python_button.click()

    else:
        print("I have failed you sensei!")


def q3(i):
    if dataset['inq_yr'][i] == 0:
        python_button = driver.find_element_by_xpath("//button[@data-answer='3_a'] ")
        python_button.click()

    elif dataset['inq_yr'][i] == 1:
        python_button = driver.find_element_by_xpath("//button[@data-answer='3_b'] ")
        python_button.click()

    elif dataset['inq_yr'][i] == 2:
        python_button = driver.find_element_by_xpath("//button[@data-answer='3_c'] ")
        python_button.click()

    elif dataset['inq_yr'][i] >= 3 and dataset['inq_yr'][i] <= 5:
        python_button = driver.find_element_by_xpath("//button[@data-answer='3_d'] ")
        python_button.click()

    elif dataset['inq_yr'][i] >= 6:
        python_button = driver.find_element_by_xpath("//button[@data-answer='3_e'] ")
        python_button.click()

    else:
        print("I have failed you sensei!")


def q4(i):
    if dataset['recent_account'][i] < 0.25:
        python_button = driver.find_element_by_xpath("//button[@data-answer='4_a'] ")
        python_button.click()

    elif dataset['recent_account'][i] >= 0.25 and dataset['recent_account'][i] <= 0.5:
        python_button = driver.find_element_by_xpath("//button[@data-answer='4_b'] ")
        python_button.click()

    elif dataset['recent_account'][i] > 0.5:
        python_button = driver.find_element_by_xpath("//button[@data-answer='4_c'] ")
        python_button.click()

    else:
        print("I have failed you sensei!")


def q5(i):
    if dataset['accnts_with_bal'][i] >= 0 and dataset['accnts_with_bal'][i] <= 4:
        python_button = driver.find_element_by_xpath("//button[@data-answer='5_a'] ")
        python_button.click()

    elif dataset['accnts_with_bal'][i] >= 5 and dataset['accnts_with_bal'][i] <= 6:
        python_button = driver.find_element_by_xpath("//button[@data-answer='5_b'] ")
        python_button.click()

    elif dataset['accnts_with_bal'][i] >= 7 and dataset['accnts_with_bal'][i] <= 8:
        python_button = driver.find_element_by_xpath("//button[@data-answer='5_c'] ")
        python_button.click()

    elif dataset['accnts_with_bal'][i] >= 9:
        python_button = driver.find_element_by_xpath("//button[@data-answer='5_d'] ")
        python_button.click()

    else:
        print("I have failed you sensei!")


def q6(i):
    if dataset['amount_owe(!m)'][i] < 500:
        python_button = driver.find_element_by_xpath("//button[@data-answer='6_b'] ")
        python_button.click()

    elif dataset['amount_owe(!m)'][i] >= 500 and dataset['amount_owe(!m)'][i] <= 999:
        python_button = driver.find_element_by_xpath("//button[@data-answer='6_c'] ")
        python_button.click()

    elif dataset['amount_owe(!m)'][i] >= 1000 and dataset['amount_owe(!m)'][i] <= 4999:
        python_button = driver.find_element_by_xpath("//button[@data-answer='6_d'] ")
        python_button.click()

    elif dataset['amount_owe(!m)'][i] >= 5000 and dataset['amount_owe(!m)'][i] <= 9999:
        python_button = driver.find_element_by_xpath("//button[@data-answer='6_e'] ")
        python_button.click()

    elif dataset['amount_owe(!m)'][i] >= 10000 and dataset['amount_owe(!m)'][i] <= 19999:
        python_button = driver.find_element_by_xpath("//button[@data-answer='6_f'] ")
        python_button.click()

    elif dataset['amount_owe(!m)'][i] >= 20000:
        python_button = driver.find_element_by_xpath("//button[@data-answer='6_g'] ")
        python_button.click()

    else:
        print("I have failed you sensei!")


def q7(i):
    if dataset['recent_delinq'][i] == 0:
        python_button = driver.find_element_by_xpath("//button[@data-answer='7_a'] ")
        python_button.click()

    elif dataset['recent_delinq'][i] < 3:
        python_button = driver.find_element_by_xpath("//button[@data-answer='7_b'] ")
        python_button.click()
        q7_2(i)
    elif dataset['recent_delinq'][i] >= 3 and dataset['recent_delinq'][i] < 6:
        python_button = driver.find_element_by_xpath("//button[@data-answer='7_c'] ")
        python_button.click()
        q7_2(i)
    elif dataset['recent_delinq'][i] >= 6 and dataset['recent_delinq'][i] < 12:
        python_button = driver.find_element_by_xpath("//button[@data-answer='7_d'] ")
        python_button.click()
        q7_2(i)
    elif dataset['recent_delinq'][i] >= 12 and dataset['recent_delinq'][i] < 24:
        python_button = driver.find_element_by_xpath("//button[@data-answer='7_e'] ")
        python_button.click()
        q7_2(i)
    elif dataset['recent_delinq'][i] >= 24 and dataset['recent_delinq'][i] < 36:
        python_button = driver.find_element_by_xpath("//button[@data-answer='7_f'] ")
        python_button.click()
        q7_2(i)
    elif 36 <= dataset['recent_delinq'][i] < 48:
        python_button = driver.find_element_by_xpath("//button[@data-answer='7_g'] ")
        python_button.click()
        q7_2(i)
    elif dataset['recent_delinq'][i] >= 48:
        python_button = driver.find_element_by_xpath("//button[@data-answer='7_h'] ")
        python_button.click()
        q7_2(i)
    else:
        print("I have failed you sensei!")


def q7_2(i):
    if 0 <= dataset['max_delinq'][i] <= 1:
        python_button = driver.find_element_by_xpath("//button[@data-answer='7a_a'] ")
        python_button.click()

    elif dataset['max_delinq'][i] == 2:
        python_button = driver.find_element_by_xpath("//button[@data-answer='7a_b'] ")
        python_button.click()
    elif dataset['max_delinq'][i] == 3:
        python_button = driver.find_element_by_xpath("//button[@data-answer='7a_c'] ")
        python_button.click()

    elif dataset['max_delinq'][i] > 3:
        python_button = driver.find_element_by_xpath("//button[@data-answer='7a_d'] ")
        python_button.click()

    else:
        print("I have failed you sensei!")


def q8(i):
    if dataset['count_od'][i] == 0:
        python_button = driver.find_element_by_xpath("//button[@data-answer='8_a'] ")
        python_button.click()

    elif dataset['count_od'][i] == 1:
        python_button = driver.find_element_by_xpath("//button[@data-answer='8_b'] ")
        python_button.click()
        q8_2(i)
    elif dataset['count_od'][i] >= 2:
        python_button = driver.find_element_by_xpath("//button[@data-answer='8_c'] ")
        python_button.click()
        q8_2(i)
    else:
        print("I have failed you sensei!")


def q8_2(i):
    if dataset['amt_od'][i] < 250:
        python_button = driver.find_element_by_xpath("//button[@data-answer='8a_a'] ")
        python_button.click()

    elif dataset['amt_od'][i] >= 250 and dataset['amt_od'][i] < 500:
        python_button = driver.find_element_by_xpath("//button[@data-answer='8a_b'] ")
        python_button.click()

    elif dataset['amt_od'][i] >= 500 and dataset['amt_od'][i] < 5000:
        python_button = driver.find_element_by_xpath("//button[@data-answer='8a_c'] ")
        python_button.click()

    elif dataset['amt_od'][i] >= 5000:
        python_button = driver.find_element_by_xpath("//button[@data-answer='8a_d'] ")
        python_button.click()

    else:
        print("I have failed you sensei!")


def q9(i):
    if 0 <= dataset['perc_climit'][i] <= 9:
        python_button = driver.find_element_by_xpath("//button[@data-answer='9_b'] ")
        python_button.click()

    elif dataset['perc_climit'][i] >= 10 and dataset['perc_climit'][i] <= 19:
        python_button = driver.find_element_by_xpath("//button[@data-answer='9_c'] ")
        python_button.click()

    elif dataset['perc_climit'][i] >= 20 and dataset['perc_climit'][i] <= 29:
        python_button = driver.find_element_by_xpath("//button[@data-answer='9_d'] ")
        python_button.click()

    elif dataset['perc_climit'][i] >= 30 and dataset['perc_climit'][i] <= 39:
        python_button = driver.find_element_by_xpath("//button[@data-answer='9_e'] ")
        python_button.click()

    elif dataset['perc_climit'][i] >= 40 and dataset['perc_climit'][i] <= 49:
        python_button = driver.find_element_by_xpath("//button[@data-answer='9_f'] ")
        python_button.click()

    elif dataset['perc_climit'][i] >= 50 and dataset['perc_climit'][i] <= 69:
        python_button = driver.find_element_by_xpath("//button[@data-answer='9_g'] ")
        python_button.click()

    elif dataset['perc_climit'][i] >= 70 and dataset['perc_climit'][i] <= 89:
        python_button = driver.find_element_by_xpath("//button[@data-answer='9_h'] ")
        python_button.click()

    elif dataset['perc_climit'][i] >= 90 and dataset['perc_climit'][i] <= 99:
        python_button = driver.find_element_by_xpath("//button[@data-answer='9_i'] ")
        python_button.click()

    elif dataset['perc_climit'][i] >= 100:
        python_button = driver.find_element_by_xpath("//button[@data-answer='9_j'] ")
        python_button.click()

    else:
        print("I have failed you sensei!")


def q10(i):
    if dataset['num_badcred'][i] == 0:
        python_button = driver.find_element_by_xpath("//button[@data-answer='10_a'] ")
        python_button.click()
        q10_2(i)

    elif dataset['num_badcred'][i] > 0:
        python_button = driver.find_element_by_xpath("//button[@data-answer='10_b'] ")
        python_button.click()


    else:
        print("I have failed you sensei!")


def q10_2(i):
    if dataset['rec_badcred'][i] < 1:
        python_button = driver.find_element_by_xpath("//button[@data-answer='10a_a'] ")
        python_button.click()
    elif 1 <= dataset['rec_badcred'][i] <= 3:
        python_button = driver.find_element_by_xpath("//button[@data-answer='10a_b'] ")
        python_button.click()
    elif dataset['rec_badcred'] > 3:
        python_button = driver.find_element_by_xpath("//button[@data-answer='10a_c'] ")
        python_button.click()
    else:
        print("I have failed you sensei!")



dataset = pd.read_csv('get_score.csv')
dataset = dataset.fillna(0)

x = len(dataset)

def main():
    for i in range(88051, x):
        if dataset['number_cc'][i] == 0:
            python_button = driver.find_element_by_xpath("//button[@data-answer='1_a'] ")
            python_button.click()

            q2(i)

            q3(i)

            q4(i)

            q5(i)

            q6(i)

            q7(i)

            q8(i)

            q9(i)

            q10(i)
            time.sleep(1)

            score(i)
            python_button = driver.find_element_by_xpath("//button[@data-cs-name='estimator.start.over']")
            python_button.click()

        elif dataset['number_cc'][i] == 1:

            python_button = driver.find_element_by_xpath("//button[@data-answer='1_b'] ")
            python_button.click()

            q1_2(i)

            q3(i)

            q4(i)

            q5(i)

            q6(i)

            q7(i)

            q8(i)

            q9(i)

            q10(i)
            time.sleep(1)

            score(i)

            python_button = driver.find_element_by_xpath("//button[@data-cs-name='estimator.start.over']")
            python_button.click()

        elif dataset['number_cc'][i] >= 2 and dataset['number_cc'][i] <= 4:

            python_button = driver.find_element_by_xpath("//button[@data-answer='1_c'] ")
            python_button.click()

            q1_2(i)

            q3(i)

            q4(i)

            q5(i)

            q6(i)

            q7(i)

            q8(i)

            q9(i)

            q10(i)
            time.sleep(1)

            score(i)

            python_button = driver.find_element_by_xpath("//button[@data-cs-name='estimator.start.over']")
            python_button.click()

        elif dataset['number_cc'][i] >= 5:

            python_button = driver.find_element_by_xpath("//button[@data-answer='1_d'] ")
            python_button.click()

            q1_2(i)

            q3(i)

            q4(i)

            q5(i)

            q6(i)

            q7(i)

            q8(i)

            q9(i)

            q10(i)
            time.sleep(1)

            score(i)

            python_button = driver.find_element_by_xpath("//button[@data-cs-name='estimator.start.over']")
            python_button.click()

        else:
            print("i have failed")


if __name__ == "__main__":
    main()
