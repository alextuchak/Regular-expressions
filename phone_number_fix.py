import re
from ReaderWriter import ReaderWriter


class PhoneNumberFix:

    reader = ReaderWriter('reader')

    def __init__(self, name):
        self.name = name

    def numb_fix(self):
        fixed_numb_format = []
        contacts_list = ReaderWriter.reader(PhoneNumberFix.reader)
        phone_pattern1 = re.compile(r"(\+7|8)\s*\(?(\d{1,3})\)?\s*-?(\d{1,3})-?(\d{1,2})-?(\d+) *\(?(доб.)? ?(\d+)?\)?")
        templist = []
        for lists in contacts_list:
            for el in lists:
                templist.append(phone_pattern1.sub(r"+7(\2)-\3-\4-\5 \6\7", el))
            fixed_numb_format.append(templist)
            templist = []
        return fixed_numb_format
