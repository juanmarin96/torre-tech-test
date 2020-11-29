import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-create-post-dialog',
  templateUrl: './create-post-dialog.component.html',
  styleUrls: ['./create-post-dialog.component.scss']
})
export class CreatePostDialogComponent implements OnInit {

  postImage;
  constructor() { }

  ngOnInit(): void {
  }

  onFileInput(event){
    var tgt = event.target || window.event.srcElement,
    files = tgt.files;

    if (FileReader && files && files.length) {
      var fr = new FileReader();
      fr.onload = (_event) =>{
        this.postImage = fr.result;
      }
      fr.readAsDataURL(files[0]);
  }
  }

}
