### Hi there.

Welcome To Introducing Chat2Bot:RICOLA
 
 
 PROBLEMS:
  문제_1: 우리는 가끔 keyboard에서 다른 국가의 언어 keyboard 없는 경우도 있고 똑 같은 말을 다른 언어로 글자로 써서 보내주면도 상대방이 이해되지 못할 수도 있다. (예: Nice(eng)----->나이스(kr/ 한국어를 모르면 영국인이 나이스라는 말을 이해하지 못한다), 땡큐(kr)------> Thank You(Eng)... etc)
  문제_2: 언어 마다 소소한 근데 중요함을 가지고 있는 점들, 외우기가 힘들거나 기억하는 게 어려운 점 있는 게 당연한다. (예: 오류 or 어류, 에콰도르  or 애콰도르, 에스컬레이터 or 애스컬래이터 else or 에스컬레이토 ?????)
  문제_3: 욕설이나 악플 정료가 다양해서 가끔 이런 단어를 chat에서 빼버리는 게 좋지 않을까?
  
  
What is the Ricola?
    
   장점_1: 가끔 사람들이 한 언어의 말을 다른 언어로 쓰는 적이 있다, 예를 들면 똑 같은 말을 바름이 비슷하게 다른 언어 글자로 쓸 수가 있다. 우리 CIS 국가들에서도 러시아어로 된 말을 latin 글자로 써서 보내드려도 친구가 이해될 수 있다. 근데 이해되지 못한 경우도 있다. 이런 경우는 이 python code로 쉽게 바꿔서 바로 보내드릴 수가 있다.
   장점_2: 그리고 가끔은 2 면 사람이 태화할 때 자기가 모르게 역 같은 말이나 악플을 보낼 수가 있다. 이 code로 우리가 악플 같은 단어를 빼고 보내줄 수가 있고 생긴 세로운 악플 단어나 욕설을 text에서 빼고 바르게 보낼 수가 있다.
   장점_3: 가끔 컴퓨터 keyboard에서 우리에게 필요한 alphabet가 없는 경우도 있다. 예를 들면: 한국에서 컴퓨터 keyboard에서 한국어-영어, 한국어만, 영어만 있는 keyboard로 도어있다. 근데 외국 사람이라면 한국어-영어-다른 언어 keyboard가 필요한다. 한국어-러시아어, 영어-러시아어, 한국어-영어-러시아어 등등... 이럴 때는 우리가 바름하는 때로 쓰면 이 단어를 우리 algorithm은 바로 이해되고 필요한 언어 alphabet으로 보내준다.
   장점_4: 러시아어에서 다들 위해 어려운 점이 있다. 한국어와(ㅗ/ㅓ, ㅐ/ㅔ) 마잔가지로 러시어에서도 ь,Ь 및 ъ,Ъ 쉽게 햇갈릴 수 있는 부분이 있다.이 CODE가 그런 글자가 있는 단어가 나오면 CODE에서 있는 단어들 중에서 찾아서 바른 단어로 바꾸어서 보내드릴 수가 있다. (이부분이 아직 개발 중...)
   
   
How do I use this?

   import telebot #대부분 CIS국가들에서 KAKAOTALK 같은 TELEGRAM app을 쓴다. So 이 python에서 된 code를 telegram app에서 실행하는 것이 많은 사람들에게 도우미 될 수 있다.
   
   import cyrtranslit   #우리에게 필요한 main algorithm을 제공해준다.
   
   from nltk.tokenize import word_tokenize  #우리 말을 받고 바꿔주는 algorithm.
   
   def get_user_text(message):   #telegram에서 메시지를 받고 word_tokenize에세 보내주는 algorithm.
   
   
   
 In Progress:
 
     1) 러시아어에서 ь,Ь 및 ъ,Ъ 글자가 있는 단어가 나무 많아서 자기 코드에다가 아직 russian_word_date 및 source을 도입하지 않았다. 개발 중...
     
 
 Resources and links:
 
 
1) https://github.com/opendatakosovo/cyrillic-transliteration
2) TELEGRAM: @Javo2Bot
3) https://desktop.telegram.org/
4) https://web.telegram.org/z/#5121709294
 
