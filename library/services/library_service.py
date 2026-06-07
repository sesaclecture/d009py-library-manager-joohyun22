
from __future__ import annotations
from typing import Iterable, List
from library.models.book import Book
from library.services.base_service import BaseService


class LibraryService(BaseService):
    """도서 목록을 메모리에서 관리하는 서비스.
    TODO:
      - 내부 상태를 캡슐화하기 위해 _books(list[Book])를 사용
      - add_book/remove_book/list_books/find_book 구현
      - 존재하지 않는 책 삭제/검색 시 ValueError 발생
    """

    def __init__(self) -> None:
        # TODO: 내부 리스트 초기화
        self._books: List[Book] = []

    def add_book(self, book: Book) -> None:
        # TODO: 책 추가
        self._books.append(book)

    def remove_book(self, title: str) -> None:
        # TODO: 제목으로 책 삭제 (없으면 ValueError)
        book = self.find_book(title)
        self._books.remove(book)

    def list_books(self) -> Iterable[Book]:
        # TODO: 책 목록 반환 (복사본 반환 권장)
        return list(self._books)

    def find_book(self, title: str) -> Book:
        # TODO: 제목으로 책 찾기 (없으면 ValueError)
        for book in self._books:
            if book.title == title:
                return book
            raise ValueError(f"{title} 이라는 책이 없습니다!")
