import { Pipe, PipeTransform } from '@angular/core';
import {isNullOrUndefined} from "util";
import {Books} from "../models/books";

@Pipe({
  name: 'sortBooks'
})
export class SortBooksPipe implements PipeTransform {

  transform(books: Books[], sortType: string, sortOrder: number): any {
    if (!isNullOrUndefined(books)) {
      if (sortType === "id") {
        books.sort((a, b) => (sortOrder)?(a.id - b.id):(b.id - a.id));
      }
      else
      if (sortType === "name") {
        books.sort((a, b) => (sortOrder)? ((a.name < b.name) ? -1 : 1):((a.name < b.name) ? 1 : -1));
      }
      else
      if (sortType === "type") {
        books.sort((a, b) => (sortOrder)?(a.type - b.type):(b.type - a.type));
      }
    }
    return books;
  }

}
