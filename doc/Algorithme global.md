
<<<<<<< HEAD



<!DOCTYPE html>
<html lang="en" class="">
  <head prefix="og: http://ogp.me/ns# fb: http://ogp.me/ns/fb# object: http://ogp.me/ns/object# article: http://ogp.me/ns/article# profile: http://ogp.me/ns/profile#">
    <meta charset='utf-8'>
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta http-equiv="Content-Language" content="en">
    
    
    <title>OpenPS/Algorithme global.md at master · Bramas/OpenPS</title>
    <link rel="search" type="application/opensearchdescription+xml" href="/opensearch.xml" title="GitHub">
    <link rel="fluid-icon" href="https://github.com/fluidicon.png" title="GitHub">
    <link rel="apple-touch-icon" sizes="57x57" href="/apple-touch-icon-114.png">
    <link rel="apple-touch-icon" sizes="114x114" href="/apple-touch-icon-114.png">
    <link rel="apple-touch-icon" sizes="72x72" href="/apple-touch-icon-144.png">
    <link rel="apple-touch-icon" sizes="144x144" href="/apple-touch-icon-144.png">
    <meta property="fb:app_id" content="1401488693436528">

      <meta content="@github" name="twitter:site" /><meta content="summary" name="twitter:card" /><meta content="Bramas/OpenPS" name="twitter:title" /><meta content="OpenPS - Open source version of the game Panic Station" name="twitter:description" /><meta content="https://avatars0.githubusercontent.com/u/835068?v=3&amp;s=400" name="twitter:image:src" />
<meta content="GitHub" property="og:site_name" /><meta content="object" property="og:type" /><meta content="https://avatars0.githubusercontent.com/u/835068?v=3&amp;s=400" property="og:image" /><meta content="Bramas/OpenPS" property="og:title" /><meta content="https://github.com/Bramas/OpenPS" property="og:url" /><meta content="OpenPS - Open source version of the game Panic Station" property="og:description" />

      <meta name="browser-stats-url" content="/_stats">
    <link rel="assets" href="https://assets-cdn.github.com/">
    <link rel="conduit-xhr" href="https://ghconduit.com:25035">
    <link rel="xhr-socket" href="/_sockets">
    <meta name="pjax-timeout" content="1000">
    <link rel="sudo-modal" href="/sessions/sudo_modal">

    <meta name="msapplication-TileImage" content="/windows-tile.png">
    <meta name="msapplication-TileColor" content="#ffffff">
    <meta name="selected-link" value="repo_source" data-pjax-transient>
      <meta name="google-analytics" content="UA-3769691-2">

    <meta content="collector.githubapp.com" name="octolytics-host" /><meta content="collector-cdn.github.com" name="octolytics-script-host" /><meta content="github" name="octolytics-app-id" /><meta content="B0B35F0A:706E:FD87404:54639EF3" name="octolytics-dimension-request_id" /><meta content="9675358" name="octolytics-actor-id" /><meta content="mickanubis" name="octolytics-actor-login" /><meta content="cae0a3806fb5a0684123e27f1d7829992d049444cf6c62ab43b28bc0a6efca1e" name="octolytics-actor-hash" />
    
    <meta content="Rails, view, blob#show" name="analytics-event" />

    
    
    <link rel="icon" type="image/x-icon" href="https://assets-cdn.github.com/favicon.ico">


    <meta content="authenticity_token" name="csrf-param" />
<meta content="rRQ7/KSKXZL/NmcRl2H+Pil6ehvYlR9xD9WDhk1bDshYwBVRS5sLxPpJKEPK/6Gm8t5plkIsfFnj4468dA/L5w==" name="csrf-token" />

    <link href="https://assets-cdn.github.com/assets/github-406b1166f1875359f0e3160125da624d5c043af14aa6d618ec9c906632b95aaa.css" media="all" rel="stylesheet" type="text/css" />
    <link href="https://assets-cdn.github.com/assets/github2-ff34ef52da60232828853c6784bb93c166f9559d854b8ae2e71598ba617af5a1.css" media="all" rel="stylesheet" type="text/css" />
    
    


    <meta http-equiv="x-pjax-version" content="c24b4447686114db6cbe58391ad15b70">

      
  <meta name="description" content="OpenPS - Open source version of the game Panic Station">
  <meta name="go-import" content="github.com/Bramas/OpenPS git https://github.com/Bramas/OpenPS.git">

  <meta content="835068" name="octolytics-dimension-user_id" /><meta content="Bramas" name="octolytics-dimension-user_login" /><meta content="26483155" name="octolytics-dimension-repository_id" /><meta content="Bramas/OpenPS" name="octolytics-dimension-repository_nwo" /><meta content="true" name="octolytics-dimension-repository_public" /><meta content="false" name="octolytics-dimension-repository_is_fork" /><meta content="26483155" name="octolytics-dimension-repository_network_root_id" /><meta content="Bramas/OpenPS" name="octolytics-dimension-repository_network_root_nwo" />
  <link href="https://github.com/Bramas/OpenPS/commits/master.atom" rel="alternate" title="Recent Commits to OpenPS:master" type="application/atom+xml">

  </head>


  <body class="logged_in  env-production windows vis-public page-blob">
    <a href="#start-of-content" tabindex="1" class="accessibility-aid js-skip-to-content">Skip to content</a>
    <div class="wrapper">
      
      
      
      


      <div class="header header-logged-in true" role="banner">
  <div class="container clearfix">

    <a class="header-logo-invertocat" href="https://github.com/" data-hotkey="g d" aria-label="Homepage" ga-data-click="Header, go to dashboard, icon:logo">
  <span class="mega-octicon octicon-mark-github"></span>
</a>


      <div class="site-search repo-scope js-site-search" role="search">
          <form accept-charset="UTF-8" action="/Bramas/OpenPS/search" class="js-site-search-form" data-global-search-url="/search" data-repo-search-url="/Bramas/OpenPS/search" method="get"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /></div>
  <input type="text"
    class="js-site-search-field is-clearable"
    data-hotkey="s"
    name="q"
    placeholder="Search"
    data-global-scope-placeholder="Search GitHub"
    data-repo-scope-placeholder="Search"
    tabindex="1"
    autocapitalize="off">
  <div class="scope-badge">This repository</div>
</form>
      </div>
      <ul class="header-nav left" role="navigation">
        <li class="header-nav-item explore">
          <a class="header-nav-link" href="/explore" data-ga-click="Header, go to explore, text:explore">Explore</a>
        </li>
          <li class="header-nav-item">
            <a class="header-nav-link" href="https://gist.github.com" data-ga-click="Header, go to gist, text:gist">Gist</a>
          </li>
          <li class="header-nav-item">
            <a class="header-nav-link" href="/blog" data-ga-click="Header, go to blog, text:blog">Blog</a>
          </li>
        <li class="header-nav-item">
          <a class="header-nav-link" href="https://help.github.com" data-ga-click="Header, go to help, text:help">Help</a>
        </li>
      </ul>

    
<ul class="header-nav user-nav right" id="user-links">
  <li class="header-nav-item dropdown js-menu-container">
    <a class="header-nav-link name" href="/mickanubis" data-ga-click="Header, go to profile, text:username">
      <img alt="mickanubis" class="avatar" data-user="9675358" height="20" src="https://avatars2.githubusercontent.com/u/9675358?v=3&amp;s=40" width="20" />
      <span class="css-truncate">
        <span class="css-truncate-target">mickanubis</span>
      </span>
    </a>
  </li>

  <li class="header-nav-item dropdown js-menu-container">
    <a class="header-nav-link js-menu-target tooltipped tooltipped-s" href="#" aria-label="Create new..." data-ga-click="Header, create new, icon:add">
      <span class="octicon octicon-plus"></span>
      <span class="dropdown-caret"></span>
    </a>

    <div class="dropdown-menu-content js-menu-content">
      
<ul class="dropdown-menu">
  <li>
    <a href="/new"><span class="octicon octicon-repo"></span> New repository</a>
  </li>
  <li>
    <a href="/organizations/new"><span class="octicon octicon-organization"></span> New organization</a>
  </li>


    <li class="dropdown-divider"></li>
    <li class="dropdown-header">
      <span title="Bramas/OpenPS">This repository</span>
    </li>
      <li>
        <a href="/Bramas/OpenPS/issues/new"><span class="octicon octicon-issue-opened"></span> New issue</a>
      </li>
</ul>

    </div>
  </li>

  <li class="header-nav-item">
        <a href="/notifications" aria-label="You have no unread notifications" class="header-nav-link notification-indicator tooltipped tooltipped-s" data-ga-click="Header, go to notifications, icon:read" data-hotkey="g n">
        <span class="mail-status all-read"></span>
        <span class="octicon octicon-inbox"></span>
</a>
  </li>

  <li class="header-nav-item">
    <a class="header-nav-link tooltipped tooltipped-s" href="/settings/profile" id="account_settings" aria-label="Settings" data-ga-click="Header, go to settings, icon:settings">
      <span class="octicon octicon-gear"></span>
    </a>
  </li>

  <li class="header-nav-item">
    <form accept-charset="UTF-8" action="/logout" class="logout-form" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="7xUofTiKayDcBbCegCQhKguHJK9U6bReQFT0k3LylJEPkNLqTSlaqWm1tzBl5kNMm5yhfAHsdNTr+qamSDfG/A==" /></div>
      <button class="header-nav-link sign-out-button tooltipped tooltipped-s" aria-label="Sign out" data-ga-click="Header, sign out, icon:logout">
        <span class="octicon octicon-sign-out"></span>
      </button>
</form>  </li>

</ul>


    
  </div>
</div>

      

        


      <div id="start-of-content" class="accessibility-aid"></div>
          <div class="site" itemscope itemtype="http://schema.org/WebPage">
    <div id="js-flash-container">
      
    </div>
    <div class="pagehead repohead instapaper_ignore readability-menu">
      <div class="container">
        
<ul class="pagehead-actions">

    <li class="subscription">
      <form accept-charset="UTF-8" action="/notifications/subscribe" class="js-social-container" data-autosubmit="true" data-remote="true" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="BnAEMZGcs4gZr/3bOv4iUyxD7tFiDaJUjA7Vey9FceVYN14+ZMWj7oXYFL96fDA0TnQf8rONncS9A9rl2Jht1w==" /></div>  <input id="repository_id" name="repository_id" type="hidden" value="26483155" />

    <div class="select-menu js-menu-container js-select-menu">
      <a class="social-count js-social-count" href="/Bramas/OpenPS/watchers">
        2
      </a>
      <a href="/Bramas/OpenPS/subscription"
        class="minibutton select-menu-button with-count js-menu-target" role="button" tabindex="0" aria-haspopup="true">
        <span class="js-select-button">
          <span class="octicon octicon-eye"></span>
          Unwatch
        </span>
      </a>

      <div class="select-menu-modal-holder">
        <div class="select-menu-modal subscription-menu-modal js-menu-content" aria-hidden="true">
          <div class="select-menu-header">
            <span class="select-menu-title">Notifications</span>
            <span class="octicon octicon-x js-menu-close" role="button" aria-label="Close"></span>
          </div> <!-- /.select-menu-header -->

          <div class="select-menu-list js-navigation-container" role="menu">

            <div class="select-menu-item js-navigation-item " role="menuitem" tabindex="0">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <div class="select-menu-item-text">
                <input id="do_included" name="do" type="radio" value="included" />
                <h4>Not watching</h4>
                <span class="description">Be notified when participating or @mentioned.</span>
                <span class="js-select-button-text hidden-select-button-text">
                  <span class="octicon octicon-eye"></span>
                  Watch
                </span>
              </div>
            </div> <!-- /.select-menu-item -->

            <div class="select-menu-item js-navigation-item selected" role="menuitem" tabindex="0">
              <span class="select-menu-item-icon octicon octicon octicon-check"></span>
              <div class="select-menu-item-text">
                <input checked="checked" id="do_subscribed" name="do" type="radio" value="subscribed" />
                <h4>Watching</h4>
                <span class="description">Be notified of all conversations.</span>
                <span class="js-select-button-text hidden-select-button-text">
                  <span class="octicon octicon-eye"></span>
                  Unwatch
                </span>
              </div>
            </div> <!-- /.select-menu-item -->

            <div class="select-menu-item js-navigation-item " role="menuitem" tabindex="0">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <div class="select-menu-item-text">
                <input id="do_ignore" name="do" type="radio" value="ignore" />
                <h4>Ignoring</h4>
                <span class="description">Never be notified.</span>
                <span class="js-select-button-text hidden-select-button-text">
                  <span class="octicon octicon-mute"></span>
                  Stop ignoring
                </span>
              </div>
            </div> <!-- /.select-menu-item -->

          </div> <!-- /.select-menu-list -->

        </div> <!-- /.select-menu-modal -->
      </div> <!-- /.select-menu-modal-holder -->
    </div> <!-- /.select-menu -->

</form>
    </li>

  <li>
    
  <div class="js-toggler-container js-social-container starring-container ">

    <form accept-charset="UTF-8" action="/Bramas/OpenPS/unstar" class="js-toggler-form starred js-unstar-button" data-remote="true" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="UdGmovrT0Tami0baM37467ggy29KxbLcUsjT6aOUodZK9Eutd4Pi6Pcui0YJfsrdvtJaJIkn7lT+z8RVUpfKvg==" /></div>
      <button
        class="minibutton with-count js-toggler-target star-button"
        aria-label="Unstar this repository" title="Unstar Bramas/OpenPS">
        <span class="octicon octicon-star"></span>
        Unstar
      </button>
        <a class="social-count js-social-count" href="/Bramas/OpenPS/stargazers">
          0
        </a>
</form>
    <form accept-charset="UTF-8" action="/Bramas/OpenPS/star" class="js-toggler-form unstarred js-star-button" data-remote="true" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="iEihg2ErmQ9OUML8su6ELY7ZALWCbP5pWogA5bonNCnZ3D5k6DKvMCC/SusqsCeRpiVET13tPOcMqEhBX9JeBg==" /></div>
      <button
        class="minibutton with-count js-toggler-target star-button"
        aria-label="Star this repository" title="Star Bramas/OpenPS">
        <span class="octicon octicon-star"></span>
        Star
      </button>
        <a class="social-count js-social-count" href="/Bramas/OpenPS/stargazers">
          0
        </a>
</form>  </div>

  </li>


        <li>
          <a href="/Bramas/OpenPS/fork" class="minibutton with-count js-toggler-target fork-button tooltipped-n" title="Fork your own copy of Bramas/OpenPS to your account" aria-label="Fork your own copy of Bramas/OpenPS to your account" rel="nofollow" data-method="post">
            <span class="octicon octicon-repo-forked"></span>
            Fork
          </a>
          <a href="/Bramas/OpenPS/network" class="social-count">0</a>
        </li>

</ul>

        <h1 itemscope itemtype="http://data-vocabulary.org/Breadcrumb" class="entry-title public">
          <span class="mega-octicon octicon-repo"></span>
          <span class="author"><a href="/Bramas" class="url fn" itemprop="url" rel="author"><span itemprop="title">Bramas</span></a></span><!--
       --><span class="path-divider">/</span><!--
       --><strong><a href="/Bramas/OpenPS" class="js-current-repository" data-pjax="#js-repo-pjax-container">OpenPS</a></strong>

          <span class="page-context-loader">
            <img alt="" height="16" src="https://assets-cdn.github.com/images/spinners/octocat-spinner-32.gif" width="16" />
          </span>

        </h1>
      </div><!-- /.container -->
    </div><!-- /.repohead -->

    <div class="container">
      <div class="repository-with-sidebar repo-container new-discussion-timeline  ">
        <div class="repository-sidebar clearfix">
            
<nav class="sunken-menu repo-nav js-repo-nav js-sidenav-container-pjax js-octicon-loaders"
     role="navigation"
     data-pjax="#js-repo-pjax-container"
     data-issue-count-url="/Bramas/OpenPS/issues/counts">
  <ul class="sunken-menu-group">
    <li class="tooltipped tooltipped-w" aria-label="Code">
      <a href="/Bramas/OpenPS" aria-label="Code" class="selected js-selected-navigation-item sunken-menu-item" data-hotkey="g c" data-selected-links="repo_source repo_downloads repo_commits repo_releases repo_tags repo_branches /Bramas/OpenPS">
        <span class="octicon octicon-code"></span> <span class="full-word">Code</span>
        <img alt="" class="mini-loader" height="16" src="https://assets-cdn.github.com/images/spinners/octocat-spinner-32.gif" width="16" />
</a>    </li>

      <li class="tooltipped tooltipped-w" aria-label="Issues">
        <a href="/Bramas/OpenPS/issues" aria-label="Issues" class="js-selected-navigation-item sunken-menu-item" data-hotkey="g i" data-selected-links="repo_issues repo_labels repo_milestones /Bramas/OpenPS/issues">
          <span class="octicon octicon-issue-opened"></span> <span class="full-word">Issues</span>
          <span class="js-issue-replace-counter"></span>
          <img alt="" class="mini-loader" height="16" src="https://assets-cdn.github.com/images/spinners/octocat-spinner-32.gif" width="16" />
</a>      </li>

    <li class="tooltipped tooltipped-w" aria-label="Pull Requests">
      <a href="/Bramas/OpenPS/pulls" aria-label="Pull Requests" class="js-selected-navigation-item sunken-menu-item" data-hotkey="g p" data-selected-links="repo_pulls /Bramas/OpenPS/pulls">
          <span class="octicon octicon-git-pull-request"></span> <span class="full-word">Pull Requests</span>
          <span class="js-pull-replace-counter"></span>
          <img alt="" class="mini-loader" height="16" src="https://assets-cdn.github.com/images/spinners/octocat-spinner-32.gif" width="16" />
</a>    </li>


      <li class="tooltipped tooltipped-w" aria-label="Wiki">
        <a href="/Bramas/OpenPS/wiki" aria-label="Wiki" class="js-selected-navigation-item sunken-menu-item" data-hotkey="g w" data-selected-links="repo_wiki /Bramas/OpenPS/wiki">
          <span class="octicon octicon-book"></span> <span class="full-word">Wiki</span>
          <img alt="" class="mini-loader" height="16" src="https://assets-cdn.github.com/images/spinners/octocat-spinner-32.gif" width="16" />
</a>      </li>
  </ul>
  <div class="sunken-menu-separator"></div>
  <ul class="sunken-menu-group">

    <li class="tooltipped tooltipped-w" aria-label="Pulse">
      <a href="/Bramas/OpenPS/pulse" aria-label="Pulse" class="js-selected-navigation-item sunken-menu-item" data-selected-links="pulse /Bramas/OpenPS/pulse">
        <span class="octicon octicon-pulse"></span> <span class="full-word">Pulse</span>
        <img alt="" class="mini-loader" height="16" src="https://assets-cdn.github.com/images/spinners/octocat-spinner-32.gif" width="16" />
</a>    </li>

    <li class="tooltipped tooltipped-w" aria-label="Graphs">
      <a href="/Bramas/OpenPS/graphs" aria-label="Graphs" class="js-selected-navigation-item sunken-menu-item" data-selected-links="repo_graphs repo_contributors /Bramas/OpenPS/graphs">
        <span class="octicon octicon-graph"></span> <span class="full-word">Graphs</span>
        <img alt="" class="mini-loader" height="16" src="https://assets-cdn.github.com/images/spinners/octocat-spinner-32.gif" width="16" />
</a>    </li>
  </ul>


</nav>

              <div class="only-with-full-nav">
                
  
<div class="clone-url open"
  data-protocol-type="http"
  data-url="/users/set_protocol?protocol_selector=http&amp;protocol_type=push">
  <h3><span class="text-emphasized">HTTPS</span> clone URL</h3>
  <div class="input-group">
    <input type="text" class="input-mini input-monospace js-url-field"
           value="https://github.com/Bramas/OpenPS.git" readonly="readonly">
    <span class="input-group-button">
      <button aria-label="Copy to clipboard" class="js-zeroclipboard minibutton zeroclipboard-button" data-clipboard-text="https://github.com/Bramas/OpenPS.git" data-copied-hint="Copied!" type="button"><span class="octicon octicon-clippy"></span></button>
    </span>
  </div>
</div>

  
<div class="clone-url "
  data-protocol-type="ssh"
  data-url="/users/set_protocol?protocol_selector=ssh&amp;protocol_type=push">
  <h3><span class="text-emphasized">SSH</span> clone URL</h3>
  <div class="input-group">
    <input type="text" class="input-mini input-monospace js-url-field"
           value="git@github.com:Bramas/OpenPS.git" readonly="readonly">
    <span class="input-group-button">
      <button aria-label="Copy to clipboard" class="js-zeroclipboard minibutton zeroclipboard-button" data-clipboard-text="git@github.com:Bramas/OpenPS.git" data-copied-hint="Copied!" type="button"><span class="octicon octicon-clippy"></span></button>
    </span>
  </div>
</div>

  
<div class="clone-url "
  data-protocol-type="subversion"
  data-url="/users/set_protocol?protocol_selector=subversion&amp;protocol_type=push">
  <h3><span class="text-emphasized">Subversion</span> checkout URL</h3>
  <div class="input-group">
    <input type="text" class="input-mini input-monospace js-url-field"
           value="https://github.com/Bramas/OpenPS" readonly="readonly">
    <span class="input-group-button">
      <button aria-label="Copy to clipboard" class="js-zeroclipboard minibutton zeroclipboard-button" data-clipboard-text="https://github.com/Bramas/OpenPS" data-copied-hint="Copied!" type="button"><span class="octicon octicon-clippy"></span></button>
    </span>
  </div>
</div>


<p class="clone-options">You can clone with
      <a href="#" class="js-clone-selector" data-protocol="http">HTTPS</a>,
      <a href="#" class="js-clone-selector" data-protocol="ssh">SSH</a>,
      or <a href="#" class="js-clone-selector" data-protocol="subversion">Subversion</a>.
  <a href="https://help.github.com/articles/which-remote-url-should-i-use" class="help tooltipped tooltipped-n" aria-label="Get help on which URL is right for you.">
    <span class="octicon octicon-question"></span>
  </a>
</p>


  <a href="http://windows.github.com" class="minibutton sidebar-button" title="Save Bramas/OpenPS to your computer and use it in GitHub Desktop." aria-label="Save Bramas/OpenPS to your computer and use it in GitHub Desktop.">
    <span class="octicon octicon-device-desktop"></span>
    Clone in Desktop
  </a>

                <a href="/Bramas/OpenPS/archive/master.zip"
                   class="minibutton sidebar-button"
                   aria-label="Download the contents of Bramas/OpenPS as a zip file"
                   title="Download the contents of Bramas/OpenPS as a zip file"
                   rel="nofollow">
                  <span class="octicon octicon-cloud-download"></span>
                  Download ZIP
                </a>
              </div>
        </div><!-- /.repository-sidebar -->

        <div id="js-repo-pjax-container" class="repository-content context-loader-container" data-pjax-container>
          

<a href="/Bramas/OpenPS/blob/2db8a363fb522ed6393dcab8dd45cd432daa60a0/doc/Algorithme%20global.md" class="hidden js-permalink-shortcut" data-hotkey="y">Permalink</a>

<!-- blob contrib key: blob_contributors:v21:2247a3fadc17b2743a5dd79c86131268 -->

<div class="file-navigation">
  
<div class="select-menu js-menu-container js-select-menu left">
  <span class="minibutton select-menu-button js-menu-target css-truncate" data-hotkey="w"
    data-master-branch="master"
    data-ref="master"
    title="master"
    role="button" aria-label="Switch branches or tags" tabindex="0" aria-haspopup="true">
    <span class="octicon octicon-git-branch"></span>
    <i>branch:</i>
    <span class="js-select-button css-truncate-target">master</span>
  </span>

  <div class="select-menu-modal-holder js-menu-content js-navigation-container" data-pjax aria-hidden="true">

    <div class="select-menu-modal">
      <div class="select-menu-header">
        <span class="select-menu-title">Switch branches/tags</span>
        <span class="octicon octicon-x js-menu-close" role="button" aria-label="Close"></span>
      </div> <!-- /.select-menu-header -->

      <div class="select-menu-filters">
        <div class="select-menu-text-filter">
          <input type="text" aria-label="Find or create a branch…" id="context-commitish-filter-field" class="js-filterable-field js-navigation-enable" placeholder="Find or create a branch…">
        </div>
        <div class="select-menu-tabs">
          <ul>
            <li class="select-menu-tab">
              <a href="#" data-tab-filter="branches" class="js-select-menu-tab">Branches</a>
            </li>
            <li class="select-menu-tab">
              <a href="#" data-tab-filter="tags" class="js-select-menu-tab">Tags</a>
            </li>
          </ul>
        </div><!-- /.select-menu-tabs -->
      </div><!-- /.select-menu-filters -->

      <div class="select-menu-list select-menu-tab-bucket js-select-menu-tab-bucket" data-tab-filter="branches">

        <div data-filterable-for="context-commitish-filter-field" data-filterable-type="substring">


            <div class="select-menu-item js-navigation-item selected">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/Bramas/OpenPS/blob/master/doc/Algorithme%20global.md"
                 data-name="master"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text css-truncate-target"
                 title="master">master</a>
            </div> <!-- /.select-menu-item -->
        </div>

          <form accept-charset="UTF-8" action="/Bramas/OpenPS/branches" class="js-create-branch select-menu-item select-menu-new-item-form js-navigation-item js-new-item-form" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="mrnOW34Ad8s3s4qDiKVN3FLY9WmWxkOM0t6SUEwQ0lpkg0+tO9lqA26wkdS0Z/fq28zZx8QZwcNm/9Te24tQdw==" /></div>
            <span class="octicon octicon-git-branch select-menu-item-icon"></span>
            <div class="select-menu-item-text">
              <h4>Create branch: <span class="js-new-item-name"></span></h4>
              <span class="description">from ‘master’</span>
            </div>
            <input type="hidden" name="name" id="name" class="js-new-item-value">
            <input type="hidden" name="branch" id="branch" value="master">
            <input type="hidden" name="path" id="path" value="doc/Algorithme global.md">
          </form> <!-- /.select-menu-item -->

      </div> <!-- /.select-menu-list -->

      <div class="select-menu-list select-menu-tab-bucket js-select-menu-tab-bucket" data-tab-filter="tags">
        <div data-filterable-for="context-commitish-filter-field" data-filterable-type="substring">


        </div>

        <div class="select-menu-no-results">Nothing to show</div>
      </div> <!-- /.select-menu-list -->

    </div> <!-- /.select-menu-modal -->
  </div> <!-- /.select-menu-modal-holder -->
</div> <!-- /.select-menu -->

  <div class="button-group right">
    <a href="/Bramas/OpenPS/find/master"
          class="js-show-file-finder minibutton empty-icon tooltipped tooltipped-s"
          data-pjax
          data-hotkey="t"
          aria-label="Quickly jump between files">
      <span class="octicon octicon-list-unordered"></span>
    </a>
    <button aria-label="Copy to clipboard" class="js-zeroclipboard minibutton zeroclipboard-button" data-clipboard-text="doc/Algorithme global.md" data-copied-hint="Copied!" type="button"><span class="octicon octicon-clippy"></span></button>
  </div>

  <div class="breadcrumb">
    <span class='repo-root js-repo-root'><span itemscope="" itemtype="http://data-vocabulary.org/Breadcrumb"><a href="/Bramas/OpenPS" class="" data-branch="master" data-direction="back" data-pjax="true" itemscope="url"><span itemprop="title">OpenPS</span></a></span></span><span class="separator"> / </span><span itemscope="" itemtype="http://data-vocabulary.org/Breadcrumb"><a href="/Bramas/OpenPS/tree/master/doc" class="" data-branch="master" data-direction="back" data-pjax="true" itemscope="url"><span itemprop="title">doc</span></a></span><span class="separator"> / </span><strong class="final-path">Algorithme global.md</strong>
  </div>
</div>


  <div class="commit file-history-tease">
    <div class="file-history-tease-header">
        <img alt="mickanubis" class="avatar" data-user="9675358" height="24" src="https://avatars0.githubusercontent.com/u/9675358?v=3&amp;s=48" width="24" />
        <span class="author"><a href="/mickanubis" rel="contributor">mickanubis</a></span>
        <time datetime="2014-11-11T17:06:56Z" is="relative-time">Nov 11, 2014</time>
        <div class="commit-title">
            <a href="/Bramas/OpenPS/commit/0ff52a0eee348758cd8b6043382f6de000abc290" class="message" data-pjax="true" title="maj indentation txt algorithm">maj indentation txt algorithm</a>
        </div>
    </div>

    <div class="participation">
      <p class="quickstat">
        <a href="#blob_contributors_box" rel="facebox">
          <strong>2</strong>
           contributors
        </a>
      </p>
          <a class="avatar-link tooltipped tooltipped-s" aria-label="Bramas" href="/Bramas/OpenPS/commits/master/doc/Algorithme%20global.md?author=Bramas"><img alt="Bramas" class="avatar" data-user="835068" height="20" src="https://avatars0.githubusercontent.com/u/835068?v=3&amp;s=40" width="20" /></a>
    <a class="avatar-link tooltipped tooltipped-s" aria-label="mickanubis" href="/Bramas/OpenPS/commits/master/doc/Algorithme%20global.md?author=mickanubis"><img alt="mickanubis" class="avatar" data-user="9675358" height="20" src="https://avatars2.githubusercontent.com/u/9675358?v=3&amp;s=40" width="20" /></a>


    </div>
    <div id="blob_contributors_box" style="display:none">
      <h2 class="facebox-header">Users who have contributed to this file</h2>
      <ul class="facebox-user-list">
          <li class="facebox-user-list-item">
            <img alt="Bramas" data-user="835068" height="24" src="https://avatars2.githubusercontent.com/u/835068?v=3&amp;s=48" width="24" />
            <a href="/Bramas">Bramas</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="mickanubis" data-user="9675358" height="24" src="https://avatars0.githubusercontent.com/u/9675358?v=3&amp;s=48" width="24" />
            <a href="/mickanubis">mickanubis</a>
          </li>
      </ul>
    </div>
  </div>

<div class="file-box">
  <div class="file">
    <div class="meta clearfix">
      <div class="info file-name">
          <span>116 lines (97 sloc)</span>
          <span class="meta-divider"></span>
        <span>6.925 kb</span>
      </div>
      <div class="actions">
        <div class="button-group">
          <a href="/Bramas/OpenPS/raw/master/doc/Algorithme%20global.md" class="minibutton " id="raw-url">Raw</a>
            <a href="/Bramas/OpenPS/blame/master/doc/Algorithme%20global.md" class="minibutton js-update-url-with-hash">Blame</a>
          <a href="/Bramas/OpenPS/commits/master/doc/Algorithme%20global.md" class="minibutton " rel="nofollow">History</a>
        </div><!-- /.button-group -->

          <a class="octicon-button tooltipped tooltipped-nw"
             href="http://windows.github.com" aria-label="Open this file in GitHub for Windows">
              <span class="octicon octicon-device-desktop"></span>
          </a>

              <a class="octicon-button js-update-url-with-hash"
                 href="/Bramas/OpenPS/edit/master/doc/Algorithme%20global.md"
                 aria-label="Edit this file"
                 data-method="post" rel="nofollow" data-hotkey="e"><span class="octicon octicon-pencil"></span></a>

            <a class="octicon-button danger"
               href="/Bramas/OpenPS/delete/master/doc/Algorithme%20global.md"
               aria-label="Delete this file"
               data-method="post" data-test-id="delete-blob-file" rel="nofollow">
          <span class="octicon octicon-trashcan"></span>
        </a>
      </div><!-- /.actions -->
    </div>
    
  <div id="readme" class="blob instapaper_body">
    <article class="markdown-body entry-content" itemprop="mainContentOfPage"><h1>
<a id="user-content-openps-panic-station" class="anchor" href="#openps-panic-station" aria-hidden="true"><span class="octicon octicon-link"></span></a>OpenPS Panic Station</h1>

<h2>
<a id="user-content-algorithme-global" class="anchor" href="#algorithme-global" aria-hidden="true"><span class="octicon octicon-link"></span></a>Algorithme global</h2>

<h3>
<a id="user-content-première-partie-mise-en-place" class="anchor" href="#premi%C3%A8re-partie-mise-en-place" aria-hidden="true"><span class="octicon octicon-link"></span></a>Première partie : mise en place</h3>

<p>Plateau de jeu</p>

<ul class="task-list">
<li>On place la salle Réacteur</li>
<li>On mélange les autres cartes lieux, sauf le Nid et le Terminal</li>
<li>On insère au hasard le Terminal dans la deuxième moitié grossière de la pile de cartes lieux</li>
<li>On insère au hasard le Nid parmi les trois dernières cartes lieux</li>
</ul>

<p>Cartes objets</p>

<ul class="task-list">
<li>On isole la carte Hôte et J cartes Jerricans</li>
<li>On mélange les autres cartes objets</li>
<li>On ajoute les 2J-1 premières cartes objets au tas contenant l'Hôte et les Jerricans</li>
<li>On mélange ce tas</li>
<li>On le place sur la pioche des cartes objets</li>
</ul>

<p>Joueurs</p>

<ul class="task-list">
<li>On détermine le nombre J de joueurs</li>
<li>On associe à chaque joueur une couleur, un nom et un ordre de jeu</li>
<li>Tous les personnages obtiennent 4 points de vie</li>
<li>Tous les androïdes obtiennent un pistolet</li>
<li>Le nombre de munitions de chaque joueur est initialisé à 0</li>
<li>Tous les soldats obtiennent un lance-flammes</li>
<li>Chaque joueur pioche deux cartes</li>
<li>Tant qu'un joueur possède une carte Parasite, on place un Parasite sur la salle de Départ, on défausse la carte Parasite et le joueur pioche une carte objet</li>
<li>Le premier joueur prend le marqueur Phase des Parasites, activé</li>
</ul>

<h3>
<a id="user-content-deuxième-partie-jeu" class="anchor" href="#deuxi%C3%A8me-partie-jeu" aria-hidden="true"><span class="octicon octicon-link"></span></a>Deuxième partie : jeu</h3>

<p>En boucle:</p>

<ul class="task-list">
<li>
<p>Si le joueur en cours a le marqueur Phase des Parasites et quil est activé, on effectue la Phase des Parasites :</p>

<ul class="task-list">
<li>On décale le marqueur Phase des Parasites au joueur suivant et on le désactive</li>
<li>Toutes les portes sont fermées</li>
<li>S'il y a des Parasites en jeu, on lance 1D4 et on déplace tous les parasites selon la direction indiquée, selon les déplacements autorisés</li>
<li>Pour chaque joueur touché :

<ul class="task-list">
<li>Si le joueur possède un gilet pare-balles et au moins 6 cartes, on lui demande s'il veut l'utiliser pour chacun de ses personnages.

<ul class="task-list">
<li>Si ses deux personnages sont dans la même pièce, on demande s'il veut l'utiliser pour les deux personnages</li>
</ul>
</li>
<li>Chaque personnage touché perd 1 PV ou 2 PV selon la couleur du Parasite</li>
<li>On enlève du plateau les personnages morts

<ul class="task-list">
<li>Si un joueur a perdu ses deux personnages, il est éliminé de la partie.

<ul class="task-list">
<li>S'il possédait le marqueur Phase des Parasites, il est décalé au joueur suivant, en gardant son statut</li>
</ul>
</li>
</ul>
</li>
<li>Si les conditions de fin de partie sont réalisées, on sort de toutes les boucles</li>
</ul>
</li>
</ul>
</li>
<li><p>Si le joueur en cours a le marqueur Phase des Parasites et qu'il est désactivé, on l'active</p></li>
<li>On détermine le nombre PA de points daction du joueur en cours</li>
<li>Tant que le joueur possède au moins 1 PA :

<ul class="task-list">
<li>On affiche les actions possibles pour ce joueur :

<ul class="task-list">
<li>Si le joueur possède au moins 6 cartes et quil possède une carte jouable, afficher « Utiliser une carte »</li>
<li>Si un personnage du joueur est dans une salle qui peut être fouillée, afficher « Fouiller une pièce »</li>
<li>Si un personnage du joueur est dans une salle contenant un personnage dun autre joueur ou un parasite, et que son personnage peut attaquer, afficher « Attaquer »</li>
<li>Si un personnage du joueur est dans une salle Terminal et quil ne la pas encore activé, afficher « Activer le Terminal »</li>
<li>Si un personnage du joueur est dans une salle Infirmerie et quil ne la pas encore activée, afficher « Se soigner à lInfirmerie »</li>
<li>Si le soldat du joueur est au Nid et que le joueur possède au moins trois Jerricans, afficher « Brûler le Nid »</li>
<li>Si un personnage du joueur est dans une salle qui permet de placer la première carte du tas, ou que celle-ci ne peut être placée nulle part, afficher « Explorer »</li>
<li>Si un personnage du joueur est dans une salle qui permet de se déplacer dans une autre salle, afficher « Se déplacer »</li>
<li>S'il choisit « Utiliser une carte » :

<ul class="task-list">
<li>On déterminer les cartes utilisables..................</li>
</ul>
</li>
</ul>
</li>
<li>S'il choisit « Fouiller une pièce » :

<ul class="task-list">
<li>Si les deux personnages ne sont pas dans la même pièce, choisir une pièce</li>
<li>Si la pièce a déjà été fouillée, faire apparaître un Parasite à laide du 1D4. Sinon, indiquer quelle a été fouillée</li>
<li>Si la pièce permet la Fouille en équipe, demander au joueur S'il veut en profiter, et si oui, avec quel autre joueur

<ul class="task-list">
<li>Distribuer une carte à chacun des deux joueurs</li>
<li>Pour chaque carte Parasite tirée, placer un Parasite de la couleur disponible à laide du 1D4 et défausser la carte</li>
</ul>
</li>
<li>Si la pièce est un entrepôt :

<ul class="task-list">
<li>Donner trois cartes au joueur actif</li>
<li>Pour chaque carte Parasite tirée, placer un Parasite de la couleur disponible à laide du 1D4 et défausser la carte</li>
</ul>
</li>
<li>Sinon :

<ul class="task-list">
<li>Donner une carte au joueur actif</li>
<li>Si la carte est un Parasite, placer un Parasite de la couleur disponible à laide du 1D4 et défausser la carte</li>
</ul>
</li>
<li>Le joueur perd 1 PA</li>
</ul>
</li>
</ul>
</li>
<li>S'il choisit « Attaquer » :

<ul class="task-list">
<li>Si les deux personnages peuvent attaquer, choisir un personnage</li>
<li>Si le personnage possède plusieurs armes (pistolet/couteau), choisir une arme.</li>
<li>Si plusieurs cibles sont disponibles pour ce personnage, choisir un ennemi.</li>
<li>Si le joueur utilise le couteau, utiliser le 1D4 :

<ul class="task-list">
<li>La cible perd 1PV.</li>
</ul>
</li>
<li>Si le joueur utilise le pistolet

<ul class="task-list">
<li>la cible perd 1 PV</li>
<li>Le joueur perd une munition.</li>
</ul>
</li>
<li>Si le joueur utilise le Fusil mitrailleur, quil y a plusieurs cibles et quil a au moins 2 munitions, demander au joueur S'il veut tirer deux balles sur une cible ou une balle pour chacune de deux cibles

<ul class="task-list">
<li>S'il tire sur une seule cible et que le joueur possède une munition, la cible perd 1 PV et le joueur perd une munition</li>
<li>S'il tire sur une seule cible et que le joueur possède 2 munitions, la cible perd 2PV et le joueur perd deux munitions</li>
<li>S'il tire sur deux cibles, chaque cible perd 1 PV et le joueur perd deux munitions.</li>
</ul>
</li>
<li>On enlève du plateau les personnages morts

<ul class="task-list">
<li>Si un joueur a perdu ses deux personnages, il est éliminé de la partie. S'il possédait le marqueur Phase des Parasites, il est décalé au joueur suivant, en gardant son statut</li>
</ul>
</li>
<li>Si les conditions de fin de partie sont réalisées, on sort de toutes les boucles</li>
<li>Le joueur perd 1 PA</li>
</ul>
</li>
<li>S'il choisit « Activer le Terminal » :

<ul class="task-list">
<li>Si le joueur a un personnage sur chacun des deux terminaux, choisir lun des deux.</li>
<li>.................</li>
<li>Penser à retourner la carte !</li>
</ul>
</li>
<li>S'il choisit « Se soigner à l'Infirmerie » :

<ul class="task-list">
<li>..................</li>
<li>Penser à retourner la carte !</li>
</ul>
</li>
<li>S'il choisit « Brûler le Nid » :

<ul class="task-list">
<li>On sort de toutes les boucles</li>
</ul>
</li>
<li>S'il choisit « Explorer » :

<ul class="task-list">
<li>Si la pièce en haut de la pile des pièces peut être placée à plusieurs endroits par le joueur :

<ul class="task-list">
<li>On affiche les positions possibles et le joueur choisit l'endroit et la disposition de la pièce.</li>
</ul>
</li>
<li>Sinon:

<ul class="task-list">
<li>...............</li>
</ul>
</li>
</ul>
</li>
</ul>

<h3>
<a id="user-content-troisième-partie-détermination-des-gagnants" class="anchor" href="#troisi%C3%A8me-partie-d%C3%A9termination-des-gagnants" aria-hidden="true"><span class="octicon octicon-link"></span></a>Troisième partie : détermination des gagnants</h3>
</article>
  </div>

  </div>
</div>

<a href="#jump-to-line" rel="facebox[.linejump]" data-hotkey="l" style="display:none">Jump to Line</a>
<div id="jump-to-line" style="display:none">
  <form accept-charset="UTF-8" class="js-jump-to-line-form">
    <input class="linejump-input js-jump-to-line-field" type="text" placeholder="Jump to line&hellip;" autofocus>
    <button type="submit" class="button">Go</button>
  </form>
</div>

        </div>

      </div><!-- /.repo-container -->
      <div class="modal-backdrop"></div>
    </div><!-- /.container -->
  </div><!-- /.site -->


    </div><!-- /.wrapper -->

      <div class="container">
  <div class="site-footer" role="contentinfo">
    <ul class="site-footer-links right">
      <li><a href="https://status.github.com/">Status</a></li>
      <li><a href="https://developer.github.com">API</a></li>
      <li><a href="http://training.github.com">Training</a></li>
      <li><a href="http://shop.github.com">Shop</a></li>
      <li><a href="/blog">Blog</a></li>
      <li><a href="/about">About</a></li>

    </ul>

    <a href="/" aria-label="Homepage">
      <span class="mega-octicon octicon-mark-github" title="GitHub"></span>
    </a>

    <ul class="site-footer-links">
      <li>&copy; 2014 <span title="0.06325s from github-fe117-cp1-prd.iad.github.net">GitHub</span>, Inc.</li>
        <li><a href="/site/terms">Terms</a></li>
        <li><a href="/site/privacy">Privacy</a></li>
        <li><a href="/security">Security</a></li>
        <li><a href="/contact">Contact</a></li>
    </ul>
  </div><!-- /.site-footer -->
</div><!-- /.container -->


    <div class="fullscreen-overlay js-fullscreen-overlay" id="fullscreen_overlay">
  <div class="fullscreen-container js-suggester-container">
    <div class="textarea-wrap">
      <textarea name="fullscreen-contents" id="fullscreen-contents" class="fullscreen-contents js-fullscreen-contents js-suggester-field" placeholder=""></textarea>
    </div>
  </div>
  <div class="fullscreen-sidebar">
    <a href="#" class="exit-fullscreen js-exit-fullscreen tooltipped tooltipped-w" aria-label="Exit Zen Mode">
      <span class="mega-octicon octicon-screen-normal"></span>
    </a>
    <a href="#" class="theme-switcher js-theme-switcher tooltipped tooltipped-w"
      aria-label="Switch themes">
      <span class="octicon octicon-color-mode"></span>
    </a>
  </div>
</div>



    <div id="ajax-error-message" class="flash flash-error">
      <span class="octicon octicon-alert"></span>
      <a href="#" class="octicon octicon-x flash-close js-ajax-error-dismiss" aria-label="Dismiss error"></a>
      Something went wrong with that request. Please try again.
    </div>


      <script crossorigin="anonymous" src="https://assets-cdn.github.com/assets/frameworks-d11dde21d6ca6bcae359b045f5ff7a3524d353cc27e7c18e3386dfeb1222a1c0.js" type="text/javascript"></script>
      <script async="async" crossorigin="anonymous" src="https://assets-cdn.github.com/assets/github-473058e3906325a52d2e7d94eca1d441f20495d4220bb098afcf4e793042b881.js" type="text/javascript"></script>
      
      
  </body>
</html>

=======
#OpenPS Panic Station


##Algorithme global

Infos concernant les effectifs des marqueurs Parasites, des cartes objets et des cartes pièces :

10 marqueurs Parasites

* 5 x Parasite gris
* 5 x Parasite noir

46 cartes objets

* 12 x Jerrican
* 7 x Gilet Pare-Balles
* 6 x Munitions
* 3 x Alerte Parasite !
* 3 x Kit de Premiers Soins
* 3 x Carte magnétique
* 2 x Fusil Mitrailleur
* 2 x Grenade
* 2 x Adrénaline
* 2 x Lunette de Précision
* 2 x Couteau de Combat
* 1 x Scanner Corporel
* 1 x Hôte

20 cartes pièces (toutes différentes)

* 1 x Réacteur
* 2 x Terminal
* 1 x Nid
* 2 x Vide
* 2 x Entrepôt
* 1 x Infirmerie
* 4 x Parasite
* 4 x Fouille en Equipe
* 3 x Course


###Première partie : mise en place

Plateau de jeu

* On place la salle Réacteur
* On mélange les autres cartes lieux, sauf le Nid et le Terminal
* On insère au hasard le Terminal dans la deuxième moitié grossière de la pile de cartes lieux
* On insère au hasard le Nid parmi les trois dernières cartes lieux

Cartes objets
* On isole la carte Hôte et J cartes Jerricans
* On mélange les autres cartes objets
* On ajoute les 2J-1 premières cartes objets au tas contenant l'Hôte et les Jerricans
* On mélange ce tas
* On le place sur la pioche des cartes objets

Joueurs

* On détermine le nombre J de joueurs
* On associe à chaque joueur une couleur, un nom et un ordre de jeu
* Tous les personnages obtiennent 4 points de vie
* Tous les androïdes obtiennent un pistolet
* Le nombre de munitions de chaque joueur est initialisé à 0
* Tous les soldats obtiennent un lance-flammes
* Chaque joueur pioche deux cartes
* Tant qu'un joueur possède une carte Parasite, on place un Parasite sur la salle de Départ, on défausse la carte Parasite et le joueur pioche une carte objet
* Le premier joueur prend le marqueur Phase des Parasites, activé



###Deuxième partie : jeu

En boucle:

* Si le joueur en cours a le marqueur Phase des Parasites et quil est activé, on effectue la Phase des Parasites :
  - On décale le marqueur Phase des Parasites au joueur suivant et on le désactive
  - Toutes les portes sont fermées
  - S'il y a des Parasites en jeu, on lance 1D4 et on déplace tous les parasites selon la direction indiquée, selon les déplacements autorisés
  - Pour chaque joueur touché :
    - Si le joueur possède un gilet pare-balles et au moins 6 cartes, on lui demande s'il veut l'utiliser pour chacun de ses personnages.
      - Si ses deux personnages sont dans la même pièce, on demande s'il veut l'utiliser pour les deux personnages
    - Chaque personnage touché perd 1 PV ou 2 PV selon la couleur du Parasite
    - On enlève du plateau les personnages morts
      * Si un joueur a perdu ses deux personnages, il est éliminé de la partie.
        - S'il possédait le marqueur Phase des Parasites, il est décalé au joueur suivant, en gardant son statut
    - Si les conditions de fin de partie sont réalisées, on sort de toutes les boucles


* Si le joueur en cours a le marqueur Phase des Parasites et qu'il est désactivé, on l'active
* On détermine le nombre PA de points daction du joueur en cours
* Tant que le joueur possède au moins 1 PA :
  - On affiche les actions possibles pour ce joueur :
    - Si le joueur possède au moins 6 cartes et quil possède une carte jouable, afficher « Utiliser une carte »
    - Si un personnage du joueur est dans une salle qui peut être fouillée, afficher « Fouiller une pièce »
    - Si un personnage du joueur est dans une salle contenant un personnage dun autre joueur ou un parasite, et que son personnage peut attaquer, afficher « Attaquer »
    - Si un personnage du joueur est dans une salle Terminal et quil ne la pas encore activé, afficher « Activer le Terminal »
    - Si un personnage du joueur est dans une salle Infirmerie et quil ne la pas encore activée, afficher « Se soigner à lInfirmerie »
    - Si le soldat du joueur est au Nid et que le joueur possède au moins trois Jerricans, afficher « Brûler le Nid »
    - Si un personnage du joueur est dans une salle qui permet de placer la première carte du tas, ou que celle-ci ne peut être placée nulle part, afficher « Explorer »
    - Si un personnage du joueur est dans une salle qui permet de se déplacer dans une autre salle, afficher « Se déplacer »
    - S'il choisit « Utiliser une carte » :
      * On déterminer les cartes utilisables..................
  * S'il choisit « Fouiller une pièce » :
    - Si les deux personnages ne sont pas dans la même pièce, choisir une pièce
    - Si la pièce a déjà été fouillée, faire apparaître un Parasite à laide du 1D4. Sinon, indiquer quelle a été fouillée
    - Si la pièce permet la Fouille en équipe, demander au joueur S'il veut en profiter, et si oui, avec quel autre joueur
      - Distribuer une carte à chacun des deux joueurs
      - Pour chaque carte Parasite tirée, placer un Parasite de la couleur disponible à laide du 1D4 et défausser la carte
    - Si la pièce est un entrepôt :
      * Donner trois cartes au joueur actif
      * Pour chaque carte Parasite tirée, placer un Parasite de la couleur disponible à laide du 1D4 et défausser la carte
    - Sinon :
      * Donner une carte au joueur actif
      * Si la carte est un Parasite, placer un Parasite de la couleur disponible à laide du 1D4 et défausser la carte
    * Le joueur perd 1 PA
* S'il choisit « Attaquer » :
  - Si les deux personnages peuvent attaquer, choisir un personnage
  - Si le personnage possède plusieurs armes (pistolet/couteau), choisir une arme.
  - Si plusieurs cibles sont disponibles pour ce personnage, choisir un ennemi.
  - Si le joueur utilise le couteau, utiliser le 1D4 :
    - La cible perd 1PV.
  - Si le joueur utilise le pistolet
    - la cible perd 1 PV
    - Le joueur perd une munition.
  - Si le joueur utilise le Fusil mitrailleur, quil y a plusieurs cibles et quil a au moins 2 munitions, demander au joueur S'il veut tirer deux balles sur une cible ou une balle pour chacune de deux cibles
    - S'il tire sur une seule cible et que le joueur possède une munition, la cible perd 1 PV et le joueur perd une munition
    - S'il tire sur une seule cible et que le joueur possède 2 munitions, la cible perd 2PV et le joueur perd deux munitions
    - S'il tire sur deux cibles, chaque cible perd 1 PV et le joueur perd deux munitions.
  - On enlève du plateau les personnages morts
    - Si un joueur a perdu ses deux personnages, il est éliminé de la partie. S'il possédait le marqueur Phase des Parasites, il est décalé au joueur suivant, en gardant son statut
  - Si les conditions de fin de partie sont réalisées, on sort de toutes les boucles
  - Le joueur perd 1 PA
* S'il choisit « Activer le Terminal » :
  - Si le joueur a un personnage sur chacun des deux terminaux, choisir lun des deux.
  - .................
  - Penser à retourner la carte !
* S'il choisit « Se soigner à l'Infirmerie » :
  * ..................
  - Penser à retourner la carte !
* S'il choisit « Brûler le Nid » :
  - On sort de toutes les boucles
* S'il choisit « Explorer » :
  - Si la pièce en haut de la pile des pièces peut être placée à plusieurs endroits par le joueur :
    * On affiche les positions possibles et le joueur choisit l'endroit et la disposition de la pièce.
  - Sinon:
    * ...............


###Troisième partie : détermination des gagnants
>>>>>>> 534d3e4c59004b4618056a9c17e0fccad2219f12
