import { Component, OnInit } from '@angular/core';
import { MatDialog } from '@angular/material/dialog';
import { CreatePostDialogComponent } from '../create-post-dialog/create-post-dialog.component';

@Component({
  selector: 'app-posts-list',
  templateUrl: './posts-list.component.html',
  styleUrls: ['./posts-list.component.scss']
})
export class PostsListComponent implements OnInit {

  posts = [1,2,3,4,5];
  constructor(private dialog: MatDialog) { }

  ngOnInit(): void {
  }

  openCreatePostDialog(){
    this.dialog.open(CreatePostDialogComponent,{
      hasBackdrop: true,
      width: "500px"
    })
  }

}
