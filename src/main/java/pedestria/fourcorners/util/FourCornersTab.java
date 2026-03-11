package pedestria.fourcorners.util;

import net.minecraft.creativetab.CreativeTabs;
import net.minecraft.item.ItemStack;
import pedestria.fourcorners.init.InitItems;

public class FourCornersTab extends CreativeTabs {

	public FourCornersTab() {
		super("tabFourCorners");
		//this.setBackgroundImageName("tab_fctab_container.png");
	}

	@Override
	public ItemStack getTabIconItem() {
		// TODO Auto-generated method stub
		return new ItemStack(InitItems.WISDOM_INGOT);
	}
	
	@Override
	public ItemStack getIconItemStack() {
		// TODO Auto-generated method stub
		return new ItemStack(InitItems.WISDOM_INGOT);
	}
	
	

}
