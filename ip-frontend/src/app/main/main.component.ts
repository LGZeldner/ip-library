import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-main',
  templateUrl: './main.component.html',
  styleUrls: ['./main.component.css']
})
export class MainComponent implements OnInit {

  sortType: string; /* поле, по которому сортируем */
  sortOrder: number; /* порядок сортировки */
  constructor() { }

  ngOnInit() {
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
