import { MainLayoutComponent } from './main-layout/main-layout.component';
import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';


const routes: Routes = [
  {
    path:'home',
    component: MainLayoutComponent,
    loadChildren: () => import('./main-layout/main-layout.module').then(m => m.MainLayoutModule)
  },
  {
    path: '**',
    redirectTo: 'home/posts', pathMatch: 'full'
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
