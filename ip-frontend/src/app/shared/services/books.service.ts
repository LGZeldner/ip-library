import {Injectable, OnInit} from '@angular/core';
import {BooksApiService} from "./books-api.service";
import {isNullOrUndefined} from "util";
import {Books} from "../models/books";

@Injectable({
  providedIn: 'root'
})
export class BooksService implements OnInit{
  public books: any;
  ngOnInit() {

  }
  constructor(private booksApiService: BooksApiService) { this.getBooks();}
  async getBooks () {
    try {
      let gbooks = this.booksApiService.getBooks();
      this.books = (isNullOrUndefined(await gbooks)) ? [] : await gbooks;

    } catch (err) {
      console.log(err);
    }
  }

  async onAddBook (book: Books) {
    book.id = (this.books.length)
      ? this.books[this.books.length - 1].id + 1
      : 1;
    this.books.push(book);
    try {
      await this.booksApiService.postBooks({
        name: book.name, type: book.type, book: book.book});
    }
    catch (e) {
      console.error(e);
    }
  }
  async onEditBook (editBook: Books) {
    let editId = this.books.findIndex ((element, index, array) => {
      return (element.id === editBook.id)});
    this.books[editId] = editBook;
    try {
      await this.booksApiService.putBooks(editBook.id, {
        name: editBook.name, type: editBook.type, book: editBook.book});
    }
    catch (e) {
      console.error(e);
    }
  }
  async onDelBook (delBookId: number) {
    this.books.splice(this.books.indexOf(this.books.find((element, index, array) => {
      return (element.id === delBookId)
    })), 1); /* удалили из массива элемент */
    try {
      await this.booksApiService.deleteBooks(delBookId);
    }
    catch (e) {
      console.error(e);
    }
  }
}
