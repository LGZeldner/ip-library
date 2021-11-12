import { Injectable } from '@angular/core';
import {HttpClient, HttpHeaders} from "@angular/common/http";
import {ApiService} from "./api.service";

@Injectable({
  providedIn: 'root'
})
export class BooksApiService extends ApiService {
  header: HttpHeaders;
  url = 'books';
  constructor(httpClient: HttpClient) {
    super (httpClient);
    this.header = new HttpHeaders();
    this.header.set ('Content-type', 'application/json');
  }
  getBooks () {
    return  this.get (this.url, this.header).toPromise();
  }
  postBooks (data) {
    return this.post (this.url, data, this.header).toPromise();
  }
  putBooks (id: number, data) {
    return this.put (`${this.url}/${id}`, data, this.header).toPromise();
  }
  deleteBooks (id: number) {
    return this.delete (`${this.url}/${id}`, this.header).toPromise();
  }
}
