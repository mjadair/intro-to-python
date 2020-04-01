# *  ----- AND/OR, NOT  ------ *
# *  💻 Remember "fn" key + "f8" to run  your code

# * 🦉 Practice








# ! ⚠️Remember to comment out your practice code before attempting below, "cmd" + "/"

# ? Comment back in the "const" declarations that have been commented out below

const milkAdded = true
const waterTemp = 100
const brewed = true

# ? Write if statements to deal with following conditions:

# ? If waterTemp is below 90, log 'Boil the kettle'

if (waterTemp < 90) {
  console.log('Boil the Kettle')
}

# ? If waterTemp is above 90, but brewed is not true, log 'Still brewing' 

if (waterTemp > 90 && !brewed) {
  console.log('Still Brewing')
}

# ? If If waterTemp is above 90 and brewed is true, but milkAdded is false, log 'Needs milk!'

if (waterTemp > 90 && brewed && !milkAdded) {
  console.log('Needs Milk')
}


# ? If waterTemp is above 90 and brewed is true and milkAdded is true, log 'Tea is ready!'

if (waterTemp > 90 && brewed && milkAdded) {
  console.log('Tea is ready!')
}
