import math
import numpy as np

#start eco class
class EcoPoint:
    #declare a private variable
    _userLevel = np.array(["Entry", "Silver", "Gold", "Diamond"])
    _level = "Entry"
    _services = {
        "voice": "voice",
        "data":"data",
        "electricity":"electricity"
    }
    def __init__(self, points) -> None:
        self._total_eco_points = points
        
    def getLevel(self, eco_points):
        if self._total_eco_points <= 500:
            self._level = self._userLevel[0] # 1x
        elif self._total_eco_points <= 1000:
            self._level =  self._userLevel[1] # 2x
        elif self._total_eco_points <= 1500:
            self._level =  self._userLevel[2] # 3x
        elif self._total_eco_points <= 2000:
            self._level =  self._userLevel[3] # 3x
        return self._level
    
    def redeemReward(self, points, service):
        amount_redeemable = 0
        total_points = 0
        if(service == "voice"):
            if(self.getLevel(points) == "Entry"):
                total_points = points
                amount_redeemable = math.floor((total_points/50) * 500)
            elif(self.getLevel(points) == "Silver"):
                total_points = points * 2
                amount_redeemable = math.floor((total_points/50) * 500)
            elif(self.getLevel(points) == "Gold"):
                total_points = points * 3
                amount_redeemable = math.floor((total_points/50) * 500)
            elif(self.getLevel(points) == "Diamond"):
                total_points = points * 3
                amount_redeemable = math.floor((total_points/50) * 500)
            print ("You have been rewarded with XAF" + str(amount_redeemable) + " worth of voice calls")
        elif(service == "data" or service == "electricity"):
            if(self.getLevel(points) == "Entry"):
                total_points = points
                amount_redeemable = math.floor((total_points/10) * 500)
            elif(self.getLevel(points) == "Silver"):
                total_points = points * 2
                amount_redeemable = math.floor((total_points/10) * 100)
            elif(self.getLevel(points) == "Gold"):
                total_points = points * 3
                amount_redeemable = math.floor((total_points/10) * 100)
            elif(self.getLevel(points) == "Diamond"):
                total_points = points * 3
                amount_redeemable = math.floor((total_points/10) * 100)
            if(service == "electricity"):
                print ("You have been rewarded with XAF" + str(amount_redeemable) + " to pay your electricity bill")
            else:
                print ("You have been rewarded with XAF" + str(amount_redeemable) + " to pay buy your data bundle")

#End of Eco Class

points = int(input("Enter the amount of Eco-Points\n"))

eco_Instance = EcoPoint(points)

print("Current Level: " + str(eco_Instance.getLevel(points)))

print("Please select a service you want to redeem")
i = 1
for key, value , in eco_Instance._services.items():
    print(f"{i}. {value}")
    i += 1
select = int(input("Reply >> "))

choice = "voice"

if (select == 2):
    choice = "data"
if(select == 3):
    choice = "electricity"

eco_Instance.redeemReward(eco_Instance._total_eco_points, choice)