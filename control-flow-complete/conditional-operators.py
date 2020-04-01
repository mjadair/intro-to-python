# *  ----- AND/OR, NOT  ------ *
#  ! Navigate to the directory and type `python conditional-operators.py` to run the file

# * 🦉 Practice


# ! ⚠️Remember to comment out your practice code before attempting below, "cmd" + "/"

# ? Comment back in the "const" declarations that have been commented out below

milkAdded = True
waterTemp = 100
brewed = True

# ? Write if statements to deal with following conditions:

# ? If waterTemp is below 90, print 'Boil the kettle'

if waterTemp < 90: 
  print('Boil the Kettle')


# ? If waterTemp is above 90, but brewed is not true, print 'Still brewing' 

if waterTemp > 90 and not brewed: 
  print('Still Brewing')


# ? If If waterTemp is above 90 and brewed is true, but milkAdded is false, print 'Needs milk!'

if waterTemp > 90 and brewed and not milkAdded: 
  print('Needs Milk')



# ? If waterTemp is above 90 and brewed is true and milkAdded is true, print 'Tea is ready!'

if waterTemp > 90 and brewed and milkAdded:
  print('Tea is ready!')

