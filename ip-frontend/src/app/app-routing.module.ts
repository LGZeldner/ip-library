import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { MainComponent } from './main/main.component';
import { PagenotfoundComponent } from './pagenotfound/pagenotfound.component';
import {BooksListComponent} from "./books-list/books-list.component";
import { AboutComponent } from './about/about.component';
import { CatalogComponent } from './catalog/catalog.component';
import { LoginComponent } from './login/login.component';
import { RegistrationComponent } from './registration/registration.component';


const routes: Routes = [
	{path: '', component: CatalogComponent},
	{path: 'login', component: LoginComponent},
	{path: 'registration', component: RegistrationComponent},
	{path: 'catalog', component: CatalogComponent},
	{path: 'books-list', component: BooksListComponent},
	{path:'**', component: PagenotfoundComponent}
	];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
