from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from database import db
from strings import SEARCH, CONVERSE, PROFILE, BALANCE, NEXT, BACK, SYMBOL, YES, NO, MALE, FEMALE
from states import EditProfile


def confirm_age_majority_kb():
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    markup.add(YES, NO)
    return markup


def gender_keyboard(male: str = MALE, female: str = FEMALE):
    markup = InlineKeyboardMarkup()
    male = InlineKeyboardButton(male, callback_data='1')
    female = InlineKeyboardButton(female, callback_data='0')
    markup.add(male, female)
    return markup


def home_keyboard():
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    search = KeyboardButton(SEARCH)
    conversation = KeyboardButton(CONVERSE)
    profile = KeyboardButton(PROFILE)
    balance = KeyboardButton(BALANCE)
    markup.add(search, conversation, profile, balance)
    return markup


def city_search_kb():
    kb = InlineKeyboardMarkup(row_width=3)
    kb.add(*(InlineKeyboardButton(callback_data=city_row[0], text=city_row[1]) for city_row in db.get_cities()))
    return kb


def like_and_chat_kb(like: str, chat: str, swipe=False):
    kb = InlineKeyboardMarkup()
    like = InlineKeyboardButton(f'๐๐ป 5{SYMBOL}', callback_data=like)
    send_message = InlineKeyboardButton(f'โ๏ธ 10{SYMBOL}', callback_data=chat)
    buttons = [like, send_message]
    if swipe:
        nxt = InlineKeyboardButton(f'โก๏ธ 1{SYMBOL}', callback_data=NEXT)
        buttons.append(nxt)
    kb.add(*buttons)
    return kb


def back_to_search_btn():
    kb = InlineKeyboardMarkup()
    kb.add(InlineKeyboardButton(BACK, callback_data=NEXT))
    return kb


def like_and_more_kb(like: str, more: str, free_profile=False):
    kb = InlineKeyboardMarkup()
    profile_text = 'โะัะพัะธะปั' if free_profile else f'๐ะัะพัะธะปั 5{SYMBOL}'
    kb.add(InlineKeyboardButton(f'๐๐ป 5{SYMBOL}', callback_data=like),
           InlineKeyboardButton(profile_text, callback_data=more))
    return kb


def chat_and_more_kb(chat: str, more: str, free_profile=False):
    kb = InlineKeyboardMarkup()
    profile_text = 'โะัะพัะธะปั' if free_profile else f'๐ะัะพัะธะปั 5{SYMBOL}'
    chat_text = 'โะะฐะฟะธัะฐัั' if free_profile else f'โ 10{SYMBOL}'
    kb.add(InlineKeyboardButton(chat_text, callback_data=chat), InlineKeyboardButton(profile_text, callback_data=more))
    return kb


def chat_kb(chat: str):
    kb = InlineKeyboardMarkup()
    kb.add(InlineKeyboardButton('โ๏ธะะฐะฟะธัะฐัั', callback_data=chat))
    return kb


def profile_edit_kb():
    kb = InlineKeyboardMarkup()
    name = InlineKeyboardButton('๐ะะผั', callback_data=EditProfile.name.state)
    age = InlineKeyboardButton('๐ะะพะทัะฐัั', callback_data=EditProfile.age.state)
    city = InlineKeyboardButton('๐บ๏ธะะพัะพะด', callback_data=EditProfile.city.state)
    occupation = InlineKeyboardButton('๐ญะ?ะพะด ะทะฐะฝััะธะน', callback_data=EditProfile.occupation.state)
    about = InlineKeyboardButton('๐ะ ัะตะฑะต', callback_data=EditProfile.about.state)
    photo = InlineKeyboardButton('๐ทะคะพัะพ', callback_data=EditProfile.photo.state)
    kb.add(name, age, city, occupation, about, photo)
    return kb
