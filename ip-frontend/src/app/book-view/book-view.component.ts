import {Component, EventEmitter, Input, OnInit, Output} from '@angular/core';
import {BooksService} from "../shared/services/books.service";
import {Router} from "@angular/router";
import {Books} from "../shared/models/books";

@Component({
  selector: 'app-book-view',
  templateUrl: './book-view.component.html',
  styleUrls: ['./book-view.component.css']
})
export class BookViewComponent implements OnInit {
  @Input() inBook: Books;
  @Output() delBook = new EventEmitter<number>(); /* отправляем наверх */
  editFlag: boolean;
  constructor(public booksService: BooksService,
              private router: Router) { }

  ngOnInit() {
  }
  onDelBook () {
    this.delBook.emit(this.inBook.id);
  }

}
