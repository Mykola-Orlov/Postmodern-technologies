# Рекурсивна функція, яка приймає слово word і повертає його дзеркально розгорнуту версію
def mirror_reverse(word):
    if len(word) <= 1: # Ця умова перевіряє, чи довжина слова word є меншою або дорівнює 1.
        return word # Якщо слово складається з однієї або менше літер, функція одразу повертає це слово.
    else:
        return word[-1] + mirror_reverse(word[:-1]) # Функція рекурсивно викликається для скороченого слова
                                                    # а потім додає до результату останню літеру
# Функція перевіряє, чи є слово дзеркально розгорнутим.    
def check_mirror(word):
    # Перевірка чи містить слово лише букви
    if not word.isalpha():
        print("False (Слово має містити лише букви)")
        return
    # Перевірка чи співпадає введене слово з відзеркаленим
    reversed_word = mirror_reverse(word)
    if word == reversed_word:
        print("Try")
        print(word, reversed_word)
    else:
        print("False")
        print(word, reversed_word)

# Запуск
word = input("Введіть слово ")
check_mirror(word)