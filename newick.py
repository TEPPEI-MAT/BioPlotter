from ete3 import Tree, TreeStyle, NodeStyle

newick_data = ""

tree = Tree(newick_data)

ts = TreeStyle()
ts.show_leaf_name = True 
ts.scale = 10  
ts.mode = "c" 
def set_color(node, color):
    nstyle = NodeStyle()
    nstyle["fgcolor"] = color
    nstyle["size"] = 7      
    nstyle["vt_line_color"] = color  
    nstyle["hz_line_color"] = color 
    nstyle["vt_line_width"] = 2      
    nstyle["hz_line_width"] = 2      
    node.set_style(nstyle)

###色をつけたい場合、uniplot numberをここに入れる###
"""for leaf in tree:
    if leaf.name in ["O67050", "P68398", "A0A7C6YL97", "2o3k_A", "2o3k_B", "Q6DHV7", "Q9BUB4", "Q9JHI2"]: 
        set_color(leaf, "red") """



#tree.show(tree_style=ts)
tree.render("high_res_tree2.png", w=3840, dpi=1200, tree_style=ts)
