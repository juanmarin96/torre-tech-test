import { NgModule } from '@angular/core';
import { MainLayoutRoutingModule } from './main-layout-routing.module';
import { MainLayoutComponent } from './main-layout.component';
import { SharedModule } from '../shared/shared.module';


@NgModule({
  declarations: [MainLayoutComponent],
  imports: [
    SharedModule,
    MainLayoutRoutingModule
  ]
})
export class MainLayoutModule { }
