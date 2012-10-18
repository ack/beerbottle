
<h3>url</h3>
{{req.url}}

<h3>params</h3>
<ul>
  %for k in qs:
    <li>
      {{k}} : {{qs[k]}}
    </li>
  %end
</ul>

%rebase layout
