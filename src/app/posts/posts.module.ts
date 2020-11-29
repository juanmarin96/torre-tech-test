import { NgModule } from '@angular/core';
import { PostsRoutingModule } from './posts-routing.module';
import { SharedModule } from '../shared/shared.module';
import { PostsListComponent } from './posts-list/posts-list.component';
import { PostComponent } from './post/post.component';
import { CreatePostDialogComponent } from './create-post-dialog/create-post-dialog.component';


@NgModule({
  declarations: [PostsListComponent, PostComponent, CreatePostDialogComponent],
  imports: [
    SharedModule,
    PostsRoutingModule
  ]
})
export class PostsModule { }
