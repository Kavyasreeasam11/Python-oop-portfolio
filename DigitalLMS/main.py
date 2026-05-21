#The Digital Library Management System
#A system that tracks different types of media in a library
class Media:
    def __init__(self,title,creator):
      self.title = title
      self.creator = creator
      self.is_borrowed = False
    def borrow_media(self):
        if self.is_borrowed:
          raise ValueError("Media not available to borrow")
        else:
           self.is_borrowed=True
           print(f"Media with title {self.title} is borrowed")
    def return_media(self):
       self.is_borrowed=False   
       print(f"Media is returned")
class Book(Media):
    def __init__(self, title, creator,page_no):
      super().__init__(title, creator)
      self.page_no = page_no
    
    def __str__(self):
       return f"[Book] {self.title} by author {self.creator} ({self.page_no})"
class Magazine(Media):
    def __init__(self, title, creator,issue_number):
      super().__init__(title, creator) 
      self.issue_number = issue_number
    def __str__(self):
       return f"[Magazine] {self.title} by contributor {self.creator} , issue no is {self.issue_number}"  
class Library:
    def __init__(self,lib_name):
       self.lib_name = lib_name
       self.catalog = []
    def add_media(self,media_obj):
       self.catalog.append(media_obj)
       print(f"Added {media_obj.title} to the {self.lib_name} catalog ")
    def search_by_title(self,search_title):
        for item in self.catalog:
           if item.title.lower() == search_title.lower():
              return item
        return None
    def __len__(self):
       return len(self.catalog)
    def __getitem__(self, index):
       return self.catalog[index]
def main():
    media1 = Media("Geethanjali","Tagore")
    book1 = Book("Power of Now","Eckhart Tolle",150)
    book2 = Book("Antharmukham","Yendamuri",120)
    book3 = Book("Kite Runner","Khalid Hossain",504)
    mag1 = Magazine("India Today","Swapan Dasguptha",1009)
    mag2 = Magazine("Forbes India","Aveek Datta",1450)
    lib1 = Library("Saraswathi Digital Library")
    lib1.add_media(book1)
    lib1.add_media(book2)
    lib1.add_media(book3)
    lib1.add_media(mag1)
    lib1.add_media(mag2)  
    print(len(lib1))
    print(lib1[2])
    print(book2)
    try:
        book2.borrow_media()
        book2.borrow_media()
    except ValueError as e:
       print(e)
    book2.return_media()
if __name__ == "__main__":
    main()
    

"Initial Commit : Add digital Lib project"
