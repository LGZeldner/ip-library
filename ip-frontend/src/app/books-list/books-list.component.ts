import { Component, OnInit } from '@angular/core';
import {BooksService} from "../shared/services/books.service";

@Component({
  selector: 'app-books-list',
  templateUrl: './books-list.component.html',
  styleUrls: ['./books-list.component.css']
})
export class BooksListComponent implements OnInit {

  sortType: string; /* поле, по которому сортируем */
  sortOrder: number; /* порядок сортировки */
  constructor(public booksService: BooksService) { }

  ngOnInit() {
    this.sortIdUp();
  }
  sortIdUp(){
    this.sortType = "id";
    this.sortOrder = 1;
  }
  sortNameUp(){
    this.sortType = "name";
    this.sortOrder = 1;
  }
  sortNameDown(){
    this.sortType = "name";
    this.sortOrder = 0;
  }
  sortTypeUp(){
    this.sortType = "type";
    this.sortOrder = 1;
  }
  sortTypeDown(){
    this.sortType = "type";
    this.sortOrder = 0;
  }

}
