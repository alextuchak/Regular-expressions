from phone_number_fix import PhoneNumberFix
from ReaderWriter import ReaderWriter

class UserInfFix:
    well_done_list = []

    numb_fix = PhoneNumberFix('numb_fix')
    writer = ReaderWriter('writer')

    def __init__(self, name):
        self.name = name

    def inf_fix(self):
        contact_list = PhoneNumberFix.numb_fix(UserInfFix.numb_fix)
        templist=[]
        for i in range(0, len(contact_list)):
            templist.append(' '.join(contact_list[i][:3]).split(" ")[:3])
            templist[i].append(contact_list[i][3])
            templist[i].append(contact_list[i][4])
            templist[i].append(contact_list[i][5])
            templist[i].append(contact_list[i][6])
        self.compare(templist)


    def compare(self, templist):
        for j in range(len(templist)):
            UserInfFix.well_done_list.append([None]*len(templist[0]))
        for i in range(len(templist)):
            flag = True
            for v in range(len(templist)):
                if UserInfFix.well_done_list[v][0] == templist[i][0] and UserInfFix.well_done_list[v][1] == templist[i][1]:
                    for id, el in enumerate(UserInfFix.well_done_list[v]):
                        if el == '':
                            UserInfFix.well_done_list[v][id] = templist[i][id]
                            flag = False
            if flag == True:
                UserInfFix.well_done_list[i] = templist[i]
        self.no_repeat()

    def no_repeat(self,):

        for id, el in enumerate(UserInfFix.well_done_list):
            if el[0] == None:
                UserInfFix.well_done_list.pop(id)
        ReaderWriter.writer(UserInfFix.writer, UserInfFix.well_done_list)




