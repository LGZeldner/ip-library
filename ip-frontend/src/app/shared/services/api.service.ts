import { Injectable } from '@angular/core';
import {HttpClient, HttpHeaders} from "@angular/common/http";

@Injectable({
  providedIn: 'root'
})
export class ApiService {
  private baseUrl = "http://127.0.0.1:8000/api/"; /** Адрес api */


  constructor(public httpClient: HttpClient) { }

  private getUrl(url:string) {                    /** метод для формирования строки запроса*/
    return this.baseUrl + url;
  }

  public get(url: string, header: HttpHeaders) {

    return this.httpClient.get (this.getUrl(url));    /** метод для создания get запроса. Метод будет
     возвращать observable, который мы в дальнейшем переделаем в promise для удобства
     использования. */
  }

  public post(url: string, data, header: HttpHeaders) { /** для занесения */

    return this.httpClient.post (this.getUrl(url), data);
  }

  public put(url: string, data, header: HttpHeaders) { /** редактирование */

    return this.httpClient.put (this.getUrl(url), data);
  }

  public delete(url: string, header: HttpHeaders) { /** удаление */

    return this.httpClient.delete (this.getUrl(url));
  }
}
