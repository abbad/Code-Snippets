# // Scenario: A group of friends go on a trip together and have shared expenses. They want to settle up upon their return.
# 
# // Problem: Build a program that can input shared expenses  
# // and settle up with the minimum number of payments
# 
# // Example input: 
# // ------ ---------
# //  Abby       100  //-400  300
# //  Bill      1000  //+500  500
# //  Charles    600  //+100  700
# //  Doug       300  //-200  100
# //            1600          # this is equals to 1600 
# 
# // Expected output:
# // ---------------
# //  Abby -> Bill: 400
# //  Doug -> Bill: 100
# //  Doug -> Charles: 100
# 

from collections import namedtuple, OrderedDict
User = namedtuple('User', 'name debt')


class Books(object):

  def __init__(self, users):
    self.total = sum([user.debt for user in users])
    self.mean = self.total / len(users)
    users = dict((x, y - self.mean) for x, y in users)
    self.users = OrderedDict(sorted(users.items(), key=lambda kv: kv[1]))
    self.users_pool = list(self.users.keys())

  def settle_payments(self):
    left_index = 0
    right_index = len(self.users) - 1
    current_owing_profile  = self.users_pool[left_index]
    current_collector_profile = self.users_pool[right_index]

    while(self.users[current_owing_profile] != 0):
      debt_amount = abs(self.users[current_owing_profile])
      highest_amount = self.users[current_collector_profile]
      diff = highest_amount - debt_amount
    
      if (diff >= 0):
        print('{0}->{1}: {2}'.format(current_owing_profile, current_collector_profile, debt_amount))
        self.users[current_collector_profile] = diff
        self.users[current_owing_profile] = 0
        left_index += 1
        current_owing_profile = self.users_pool[left_index]

        if (diff == 0):
          right_index -= 1
          current_collector_profile = self.users_pool[right_index]
      else:
        print('{0}->{1}: {2}'.format(current_owing_profile, current_collector_profile, abs(diff)))
        self.users[current_collector_profile] = 0
        self.users[current_owing_profile] = diff
        right_index -= 1
        current_collector_profile = self.users_pool[right_index]
        
abby = User('Abbey', 99)
bill = User('Bill', 100)
doug = User('Doug', 50)
charles = User('Charles', 100)
users = [abby, bill, charles, doug]

Books(users).settle_payments()
