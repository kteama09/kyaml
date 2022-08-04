#############################################################################
# Generated by PAGE version 7.5
#  in conjunction with Tcl version 8.6
#  Aug 05, 2022 01:58:27 AM +03  platform: Linux
set vTcl(timestamp) ""
if {![info exists vTcl(borrow)]} {
    ::vTcl::MessageBox -title Error -message  "You must open project files from within PAGE."
    exit}


set image_list { 
}
vTcl:create_project_images $image_list   ;# In image.tcl

if {!$vTcl(borrow) && !$vTcl(template)} {

set vTcl(actual_gui_font_dft_desc)  TkDefaultFont
set vTcl(actual_gui_font_dft_name)  TkDefaultFont
set vTcl(actual_gui_font_text_desc)  TkTextFont
set vTcl(actual_gui_font_text_name)  TkTextFont
set vTcl(actual_gui_font_fixed_desc)  TkFixedFont
set vTcl(actual_gui_font_fixed_name)  TkFixedFont
set vTcl(actual_gui_font_menu_desc)  TkMenuFont
set vTcl(actual_gui_font_menu_name)  TkMenuFont
set vTcl(actual_gui_font_tooltip_desc)  TkDefaultFont
set vTcl(actual_gui_font_tooltip_name)  TkDefaultFont
set vTcl(actual_gui_font_treeview_desc)  TkDefaultFont
set vTcl(actual_gui_font_treeview_name)  TkDefaultFont
########################################### 
set vTcl(actual_gui_bg) #d9d9d9
set vTcl(actual_gui_fg) #000000
set vTcl(actual_gui_analog) #ececec
set vTcl(actual_gui_menu_analog) #ececec
set vTcl(actual_gui_menu_bg) #d9d9d9
set vTcl(actual_gui_menu_fg) #000000
set vTcl(complement_color) gray40
set vTcl(analog_color_p) #c3c3c3
set vTcl(analog_color_m) beige
set vTcl(tabfg1) black
set vTcl(tabfg2) black
set vTcl(actual_gui_menu_active_bg)  #ececec
set vTcl(actual_gui_menu_active_fg)  #000000
########################################### 
set vTcl(pr,autoalias) 1
set vTcl(pr,relative_placement) 1
set vTcl(mode) Relative
}




proc vTclWindow.top1 {base} {
    global vTcl
    if {$base == ""} {
        set base .top1
    }
    if {[winfo exists $base]} {
        wm deiconify $base; return
    }
    set top $base
    set target $base
    ###################
    # CREATING WIDGETS
    ###################
    vTcl::widgets::core::toplevel::createCmd $top -class Toplevel \
        -menu "$top.m51" -background $vTcl(actual_gui_bg) \
        -highlightcolor black 
    wm focusmodel $top passive
    wm geometry $top 589x503+308+122
    update
    # set in toplevel.wgt.
    global vTcl
    global img_list
    set vTcl(save,dflt,origin) 0
    wm maxsize $top 1351 738
    wm minsize $top 1 1
    wm overrideredirect $top 0
    wm resizable $top 1 1
    wm deiconify $top
    set toptitle "Kyaml Note-taking assistant"
    wm title $top $toptitle
    namespace eval ::widgets::${top}::ClassOption {}
    set ::widgets::${top}::ClassOption(-toptitle) $toptitle
    vTcl:DefineAlias "$top" "Toplevel1" vTcl:Toplevel:WidgetProc "" 1
    set vTcl(real_top) {}
    menu $top.m51 \
        -activebackground $vTcl(actual_gui_menu_analog) \
        -activeforeground #000000 -background $vTcl(actual_gui_menu_bg) \
        -font TkMenuFont -foreground $vTcl(actual_gui_menu_fg) -tearoff 0 
    
set site_3_0 $top.m51
    $top.m51 add cascade \
        -menu "$top.m51.men46" -command {{}} -label Notes 
    menu $site_3_0.men46 \
        -activebackground beige -activeforeground black \
        -background $vTcl(actual_gui_menu_bg) -font TkMenuFont \
        -foreground $vTcl(actual_gui_menu_fg) -tearoff 0 
    $site_3_0.men46 add command \
        -command {#} -label {New notes} 
    $site_3_0.men46 add command \
        -command {#} -label {Open a note} 
    $site_3_0.men46 add command \
        -command {#} -label Save 
    $site_3_0.men46 add command \
        -command {#} -label {Save as } 
    
set site_3_0 $top.m51
    $top.m51 add cascade \
        -menu "$top.m51.men47" -command {{}} -label Help 
    menu $site_3_0.men47 \
        -activebackground beige -activeforeground black \
        -background $vTcl(actual_gui_menu_bg) -font TkMenuFont \
        -foreground $vTcl(actual_gui_menu_fg) -tearoff 0 
    $site_3_0.men47 add command \
        -command {#} -label RTFM 
    $site_3_0.men47 add command \
        -command {#} -label About 
    ttk::style configure Treeview \
         -font  "$vTcl(actual_gui_font_treeview_desc)"
    vTcl::widgets::ttk::scrolledtreeview::CreateCmd $top.scr61 \
        -background $vTcl(actual_gui_bg) -height 15 -highlightcolor black \
        -width 30 
    vTcl:DefineAlias "$top.scr61" "Scrolledtreeview1" vTcl:WidgetProc "Toplevel1" 1

        $base.scr61.01 configure -columns "Col1 Col2" -height 4
        $base.scr61.01 configure -columns {Col1 Col2}
        $base.scr61.01 heading #0 -text {Title}
        $base.scr61.01 heading #0 -anchor center
        $base.scr61.01 column #0 -width 218
        $base.scr61.01 column #0 -minwidth 20
        $base.scr61.01 column #0 -stretch 1
        $base.scr61.01 column #0 -anchor w
        $base.scr61.01 heading Col1 -text {Note}
        $base.scr61.01 heading Col1 -anchor center
        $base.scr61.01 column Col1 -width 220
        $base.scr61.01 column Col1 -minwidth 20
        $base.scr61.01 column Col1 -stretch 1
        $base.scr61.01 column Col1 -anchor w
        $base.scr61.01 heading Col2 -text {TIme/Date}
        $base.scr61.01 heading Col2 -anchor center
        $base.scr61.01 column Col2 -width 137
        $base.scr61.01 column Col2 -minwidth 20
        $base.scr61.01 column Col2 -stretch 1
        $base.scr61.01 column Col2 -anchor w
    button $top.but63 \
        -activebackground $vTcl(analog_color_m) -activeforeground black \
        -background $vTcl(actual_gui_bg) -borderwidth 2 -compound left \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightcolor black -text + 
    vTcl:DefineAlias "$top.but63" "Button1" vTcl:WidgetProc "Toplevel1" 1
    button $top.but64 \
        -activebackground $vTcl(analog_color_m) -activeforeground black \
        -background $vTcl(actual_gui_bg) -borderwidth 2 -compound left \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightcolor black -text - 
    vTcl:DefineAlias "$top.but64" "Button2" vTcl:WidgetProc "Toplevel1" 1
    button $top.but65 \
        -activebackground $vTcl(analog_color_m) -activeforeground black \
        -background $vTcl(actual_gui_bg) -borderwidth 2 -compound left \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightcolor black -text ⮟ 
    vTcl:DefineAlias "$top.but65" "Button3" vTcl:WidgetProc "Toplevel1" 1
    button $top.but66 \
        -activebackground $vTcl(analog_color_m) -activeforeground black \
        -background $vTcl(actual_gui_bg) -borderwidth 2 -compound left \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightcolor black -text ⮝ 
    vTcl:DefineAlias "$top.but66" "Button4" vTcl:WidgetProc "Toplevel1" 1
    button $top.but67 \
        -activebackground $vTcl(analog_color_m) -activeforeground black \
        -background $vTcl(actual_gui_bg) -borderwidth 2 -compound left \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightcolor black -text ➤+ 
    vTcl:DefineAlias "$top.but67" "Button5" vTcl:WidgetProc "Toplevel1" 1
    button $top.but68 \
        -activebackground $vTcl(analog_color_m) -activeforeground black \
        -background $vTcl(actual_gui_bg) -borderwidth 2 -compound left \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightcolor black -text ➤- 
    vTcl:DefineAlias "$top.but68" "Button6" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab69 \
        -activebackground #f9f9f9 -activeforeground #000000 \
        -background $vTcl(actual_gui_bg) -compound left \
        -font {-family {DejaVu Sans} -size 10 -weight normal -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) -highlightcolor black \
        -text {Tip: Add \r \g \b to write in color} 
    vTcl:DefineAlias "$top.lab69" "Label1" vTcl:WidgetProc "Toplevel1" 1
    ###################
    # SETTING GEOMETRY
    ###################
    place $top.scr61 \
        -in $top -x 0 -y 0 -rely 0.099 -width 0 -relwidth 1 -height 0 \
        -relheight 0.899 -anchor nw -bordermode ignore 
    place $top.but63 \
        -in $top -x 0 -relx 0.016 -y 0 -rely 0.02 -width 33 -relwidth 0 \
        -height 33 -relheight 0 -anchor nw -bordermode ignore 
    place $top.but64 \
        -in $top -x 0 -relx 0.085 -y 0 -rely 0.02 -width 33 -relwidth 0 \
        -height 33 -relheight 0 -anchor nw -bordermode ignore 
    place $top.but65 \
        -in $top -x 0 -relx 0.849 -y 0 -rely 0.02 -width 33 -relwidth 0 \
        -height 33 -relheight 0 -anchor nw -bordermode ignore 
    place $top.but66 \
        -in $top -x 0 -relx 0.917 -y 0 -rely 0.02 -width 33 -relwidth 0 \
        -height 33 -relheight 0 -anchor nw -bordermode ignore 
    place $top.but67 \
        -in $top -x 0 -relx 0.153 -y 0 -rely 0.02 -width 43 -relwidth 0 \
        -height 33 -relheight 0 -anchor nw -bordermode ignore 
    place $top.but68 \
        -in $top -x 0 -relx 0.238 -y 0 -rely 0.02 -width 43 -relwidth 0 \
        -height 33 -relheight 0 -anchor nw -bordermode ignore 
    place $top.lab69 \
        -in $top -x 0 -relx 0.374 -y 0 -rely 0.02 -width 0 -relwidth 0.406 \
        -height 0 -relheight 0.062 -anchor nw -bordermode ignore 

    vTcl:FireEvent $base <<Ready>>
}

proc 36 {args} {return 1}


Window show .
set btop1 ""
if {$vTcl(borrow)} {
    set btop1 .bor[expr int([expr rand() * 100])]
    while {[lsearch $btop1 $vTcl(tops)] != -1} {
        set btop1 .bor[expr int([expr rand() * 100])]
    }
}
set vTcl(btop) $btop1
Window show .top1 $btop1
if {$vTcl(borrow)} {
    $btop1 configure -background plum
}
