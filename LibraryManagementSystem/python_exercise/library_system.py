#Task 1: Model a Book

class Book:
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author
        self.is_available = True
    
    def __str__(self):
        availability = "Available" if self.is_available else "Not Available"
        return f"'{self.title}' DE {self.author} ({availability})"


book1 = Book("1984", "George Orwell")
print(book1) 




#Task 2: Create a Library Structure
class Library:
    def __init__(self):
        self.books = []
    
    def add_book(self, title: str, author: str):
        book = Book(title, author)
        self.books.append(book)
    
    def list_books(self) -> list:
        return [str(book) for book in self.books]
    
    
   
        
        
    #Task 3: Populate the Library Dynamically
    
    def load_books(self, file_path: str):
        with open(file_path, 'r') as file:
            for line in file:
                title, author = line.strip().split(",")
                self.add_book(title, author)
                
                
    #Task 5: Handle Book Lending Logic         
    def lend_book(self, book_title: str, student: 'Student') -> bool:
        book = next((b for b in self.books if b.title == book_title and b.is_available), None)
        if book:
            book.is_available = False
            student.borrowed_books.append(book)
            print(f"{student.name} a emprunté '{book.title}'")
            return True
        else:
            print(f"Le livre {book_title} pas dispo")
            return False
    
    def accept_return(self, book_title: str, student: 'student'):
        book = next((b for b in student.borrowed_books if b.title == book_title), None)
        
        if book is None:
            print(f"{student.name} n'a pas emprunté '{book_title}' ou il n'est pas dans la liste des livres empruntés.")
            return
        
        book.is_available = True
        student.borrowed_books.remove(book)
        print(f"{student.name} a retourné '{book.title}' à la bibliothèque.")
        
   
    
    #TASK 7
    def search_books(self, query: str) -> list:
         # Recherche par titre ou auteur
         result = [str(book) for book in self.books if query.lower() in book.title.lower() or query.lower() in book.author.lower()]
         return result
        
        
    #Task 8
    def save_books(self, file_path: str):
        try:
            with open(file_path, 'w') as file:
                for book in self.books:
                    file.write(f"{book.title},{book.author},{book.is_available}\n")
            print("La bibliothèque a été sauvegardée.")
        except Exception as e:
            print(f"Erreur lors de la sauvegarde : {e}")
    
    def load_books(self, file_path: str):
        try:
            with open(file_path, 'r') as file:
                for line in file:
                    title, author, is_available = line.strip().split(',')
                    book = Book(title, author)
                    book.is_available = is_available.lower() == 'true'
                    self.books.append(book)
            print("La bibliothèque a été chargée.")
        except FileNotFoundError:
            print(f"Erreur : Le fichier {file_path} n'a pas été trouvé.")
        except Exception as e:
            print(f"Erreur lors du chargement : {e}")
            
            
            
    #TASK 9 

    def run_library_system():
        library = Library()
        student = Student("John Doe")  # Un étudiant par défaut

        while True:
            print("\n=== Menu ===")
            print("1. Voir tous les livres")
            print("2. Rechercher un livre")
            print("3. Ajouter un livre")
            print("4. Emprunter un livre")
            print("5. Retourner un livre")
            print("6. Quitter")

            choice = input("Choisissez une option (1-6): ")

            if choice == "1":
                for book in library.list_books():
                    print(book)

            elif choice == "2":
                query = input("Rechercher par titre ou auteur: ")
                results = library.search_books(query)
                if results:
                    for result in results:
                        print(result)
                else:
                    print("Aucun livre trouvé.")

            elif choice == "3":
                title = input("Titre du livre: ")
                author = input("Auteur du livre: ")
                library.add_book(title, author)
                print(f"Le livre '{title}' a été ajouté.")

            elif choice == "4":
                book_title = input("Titre du livre à emprunter: ")
                if not library.lend_book(book_title, student):
                    print(f"Impossible d'emprunter '{book_title}'.")
                else:
                    print(f"Vous avez emprunté '{book_title}'.")

            elif choice == "5":
                book_title = input("Titre du livre à retourner: ")
                library.accept_return(book_title, student)

            elif choice == "6":
                print("Au revoir!")
                break

            else:
                print("Option invalide.")





#Task 4: Introduce a Student Model

class Student:
    def __init__(self, name: str):
        self.name = name
        self.borrowed_books = []
    
    def borrow_book(self, book_title: str, library: 'Library'): 
        book = next((b for b in library.books if b.title == book_title and b.is_available), None)
        if book:
            print(f"{self.name} a emprunté '{book.title}'")
            book.is_available = False
            self.borrowed_books.append(book)
            
        else:
            print(f"'{book_title}' pas dispo ou n'existe pas")
    
    def return_book(self, book_title: str, library: 'Library'):
        book = next((b for b in self.borrowed_books if b.title == book_title), None)
        if book:
            print(f"{self.name} a RENDU '{book.title}'")
            book.is_available = True
            self.borrowed_books.remove(book)
            library.add_book(book.title, book.author)  
            
        else:
            print(f"{self.name} n'a pas emprunté '{book_title}'.")
            
            
            




#Création des objets
library = Library()
library.add_book("1984", "George Orwell")
library.add_book("Brave New World", "Aldous Huxley")
library.load_books("load_data_book.txt")

print(library.list_books())  


student = Student("John Doe")
student.borrow_book("1984", library)  
print(student.borrowed_books)  

#student.return_book("1984", library) 
#print(student.borrowed_books)


# Emprunter et Retourner un livre
library.lend_book("1984", student)
print("Avant le rendu")
print(student.borrowed_books) 
library.accept_return("1984", student)  
print("Après le rendu")
print(student.borrowed_books)  


#Utilisation TASK 7

print(library.search_books("George"))  # Recherche par auteur
print(library.search_books("1984"))   # Recherche par titre

#Utilisation TASK 8
library.save_books('library_state.txt')

new_library = Library()
new_library.load_books('library_state.txt')
print(new_library.list_books())
