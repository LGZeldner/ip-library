/* класс, описывающий книгу */
export class Books {
  public id: number; /* id */
  public name: string; /* название */
  public type: number; /* тип */
  public book: string; /* книга */
  constructor(name: string, type: number, book: string, id?: number) {
    this.id = id;
    this.name = name;
    this.type = type;
    this.book = book;
  }
}
