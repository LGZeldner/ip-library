import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { PagenotfoundComponent } from './pagenotfound/pagenotfound.component';
import { MainComponent } from './main/main.component';
import { HeaderComponent } from './header/header.component';
import { BookViewComponent } from './book-view/book-view.component';
import { BooksListComponent } from './books-list/books-list.component';
import { SortBooksPipe } from './shared/pipes/sort-books.pipe';
import { AboutComponent } from './about/about.component';
import { CatalogComponent } from './catalog/catalog.component';
import { BookPageComponent } from './book-page/book-page.component';
import { FooterComponent } from './footer/footer.component';
import { LoginComponent } from './login/login.component';
import { RegistrationComponent } from './registration/registration.component';
import { DashboardComponent } from './dashboard/dashboard.component';

@NgModule({
  declarations: [
    AppComponent,
    PagenotfoundComponent,
    MainComponent,
    HeaderComponent,
    BookViewComponent,
    BooksListComponent,
    SortBooksPipe,
    AboutComponent,
    CatalogComponent,
    BookPageComponent,
    FooterComponent,
    LoginComponent,
    RegistrationComponent,
    DashboardComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
