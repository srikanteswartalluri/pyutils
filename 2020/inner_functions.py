def outer_util(l):
   print(l)
   def stay_tuned():
      print("I am inside inner")
   stay_tuned()
   print("I am back to outer")

outer_util([1, 3, 4])
