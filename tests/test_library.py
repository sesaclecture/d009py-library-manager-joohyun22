
import pytest

#"book.py에서 Book을, library_service.py에서 LibraryService를 가져와서 쓸게"
from library.models.book import Book
from library.services.library_service import LibraryService

#테스트에서 반복적으로 쓸 책 2권을 미리 만들어두는 함수
def make_books():
    return [
        Book.from_dict({'title': '책이름', 'author': '지은이', 'year': 2000}),
        Book.from_dict({'title': '다른 책이름', 'author': '김지은', 'year': 2001}),
    ]


def test_add_and_list_books():
    svc = LibraryService() #도서관 서비스 만들기 
    for b in make_books():
        svc.add_book(b)  #책 2권 추가
    books = list(svc.list_books()) #책 목록 가져오기
    assert len(books) == 2 #책이 2권이어야 함. 
    assert books[0].title == '책이름'



def test_find_book_success_and_fail():
    svc = LibraryService()
    svc.add_book(Book.from_dict({'title': 'X', 'author': 'Y', 'year': 2000}))
    found = svc.find_book('X') #제목으로 책 찾기
    assert found.author == 'Y' #찾은 책의 저자 확인
    with pytest.raises(ValueError):
        svc.find_book('NOPE') #없는 책 찾으면 오류 발생. 



def test_remove_book():
    svc = LibraryService()
    b1, b2 = make_books()
    svc.add_book(b1)
    svc.add_book(b2)
    svc.remove_book('책이름') #책 삭제 
    books = list(svc.list_books())
    assert len(books) == 1 # 1권만 남아야함.
    assert books[0].title == '다른 책이름'
    with pytest.raises(ValueError):
        svc.remove_book('Not Exists') #없는 책 삭제하면 오류
