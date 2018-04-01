"""     
             PYTHON
             
   Product inventory manager program
   Created by:  Fon Desmond Ade
   email:  adedesmond6@gmail.com 

   Porgram functions

   - Add new products
   - Modify avaible product name
   - Deduct products from product quatity
   - Displays a particular products  quantity in stock
   - Display total amount of products available with their total quatity


   """


class Product:
	'''Use in creating a product with 
	attributes such as id, name, and quantity'''

	def __init__(self, id ,name, quantity=0):
		self.id = id
		self.name = name 
		self.quantity = quantity



class Inventory:

	def __init__(self):
		self.products = []


	def add_products(self,id, name, quantity):
		'''Adds a new product to products list'''

		self.products.append(Product(id, name, quantity))
		return self.products

	def product_quantity(self,product_name):
		'''Displays product quantity by looking
		 for product name in the list of products'''

		for product in self.products:
			if product.name == product_name:
				print(product.quantity)
				#return product.quantity
			else:
				print('That product does not exist')#Displays if products name is not found



	def modify_product_name(self,old_name, new_name):

		'''change product name by looking for all
		 product name and replacing it with new name'''

		for product in self.products:
			if product.name == old_name:
				product.name = new_name #Set product name to the new name
				print('Name succefully change')
			else:
				print('That product does not exist')



	def take_product(self,product_name, quantity):
		'''Looks for given product name in products
		   and deduct a particular quantity of that 
		   product as demanded by the user '''

		for product in self.products:
			if product.name == product_name:
				if product.quantity <= 0: # Checks to see if product is available
					print('{} product is finish'.format(product.name.capitalize()))
				elif quantity > product.quantity:#checks to makes sure quatity damanded is not greater availabe quatity
					print('Your demand is more than available products.Available Product {}'.format(product.quantity))
				else:
					product.quantity -= quantity # subtract  quatity from product quantity
					print('product succefully taken new quantity is {}'.format(product.quantity))
			else:				
				print('That product does not exist')




	def list_all_products(self):

		'''Create a new list called  new_products
		 and checks self.products for any 
		 product whose quatity is greater 0 
		 and adds it to new products. If product
		 quantity is less that zero it means that 
		 product is finish and cannot be counted 
		 as a product '''
		
		new_products = []
		for product in self.products:
			if product.quantity > 0:
				new_products.append(product)
		total_products = len(new_products) #gets the len of filtered new_products list
		                                   # and stores it the total_products variable
		print('''
			Total products is {}
			=================
			'''.format(total_products))

		for product in new_products:
			print(product.name, ' --->  {}'.format(product.quantity))





class Menu:

	def __init__(self):

		self.inventory = Inventory()



	def add_product(self):

		'''Recieves input from the user to create a new product '''

		id = int(input('Enter product id'))
		product_name = input('Enter product name')
		product_quantity = int(input('Enter product quantity'))

		self.inventory.add_products(id, product_name, product_quantity)
		print('Sucessfully added')



	def check_product_quantity(self):

		''' Recieves a product name and return
		 product quantity if product is found'''
		try:

			product_name = input('enter a product name')
			self.inventory.product_quantity(product_name)

		except Exception as e:
			print('please make sure to enter product name'.capitalize())



	def change_product_name(self):

		'''change product name by looking for all
		 product name and replacing it with new name'''
		try:

			old_name = input('Enter old product name')
			new_name = input('Enter new name')
			self.inventory.modify_product_name(old_name, new_name)

		except Exception as e:
			print('please make sure to enter old name and the new name you want'.capitalize())




	def send_out_some_products(self):

		'''Deduct some products from product
		 quantity as demanded by user'''
		try:

			product_name = input('Enter product name')
			product_quantity = int(input('Enter product quantity'))
			self.inventory.take_product(product_name, product_quantity)

		except Exception as e:
			print('please make sure to enter product name and product quantity'.capitalize())




	def show_all_products(self):
		'''Display all products to the screen'''

		self.inventory.list_all_products()




	def  display(self):

		print('''

			Welcome to Inventory Manager
			============================

			          Chioces 
			          -------

			     Enter    Function
			     -----    --------    

			     2 -------- Add new product
			     3 -------- Check product quantity
			     4 -------- Change product name
			     6 -------- Get some products
			     7 -------- See all products                



			''')

	def run(self):
		''' Ask user for a users choice and calls 
		a particular method to process user demands'''

		self.display()

		while True:
			try:

				choice = int(input('Enter your choice'))#ask for users choice

				if choice == 2:
					self.add_product()
				elif choice == 3:
					self.check_product_quantity()
				elif choice == 4:
					self.change_product_name()
				elif choice == 6:
					self.send_out_some_products()
				elif choice == 7:
					self.show_all_products()
			except Exception as e:
				print('Please you must enter a choice')

if __name__ == '__main__':
	Menu().run()

