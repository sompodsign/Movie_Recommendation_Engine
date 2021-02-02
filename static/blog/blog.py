body {
    margin:0;
    padding:0;
    font-family:helvetica, sans-serif;
}

a {
    color:#00abff;
    text-decoration:none;
}

h1 {
    font-weight:normal;
    border-bottom:1px solid #bbb;
    padding:0 0 10px 0;
}

h2 {
    font-weight:normal;
    margin:30px 0 0;
}

#content {
    float:left;
    width:60%;
    padding:0 0 0 30px;
}

#sidebar {
    float:right;
    width:30%;
    padding:10px;
    background:#efefef;
    height:100%;
}

p.date {
    color:#ccc;
    font-family: georgia, serif;
    font-size: 12px;
    font-style: italic;
}

/* pagination */
.pagination {
    margin:40px 0;
    font-weight:bold;
}

/* forms */
label {
    float:left;
    clear:both;
    color:#333;
    margin-bottom:4px;
}
input, textarea {
    clear:both;
    float:left;
    margin:0 0 10px;
    background:#ededed;
    border:0;
    padding:6px 10px;
    font-size:12px;
}
input[type=submit] {
    font-weight:bold;
    background:#00abff;
    color:#fff;
    padding:10px 20px;
    font-size:14px;
    text-transform:uppercase;
}
.errorlist {
    color:#cc0033;
    float:left;
    clear:both;
    padding-left:10px;
}

/* comments */
.comment {
    padding:10px;
}
.comment:nth-child(even) {
    background:#efefef;
}
.comment .info {
    font-weight:bold;
    font-size:12px;
    color:#666;
}