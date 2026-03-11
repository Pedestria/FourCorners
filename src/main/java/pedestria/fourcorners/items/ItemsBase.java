package pedestria.fourcorners.items;

import net.minecraft.item.Item;
import pedestria.fourcorners.FourCorners;
import pedestria.fourcorners.api.IHasModel;
import pedestria.fourcorners.init.InitItems;

public class ItemsBase extends Item implements IHasModel 
{

	public ItemsBase (String name) 
	{
		setUnlocalizedName(name);
		setRegistryName(name);
		setCreativeTab(FourCorners.fcTab);
		
		InitItems.ITEMS.add(this);
	}
	
	@Override
	public void registerModels() 
	{
		FourCorners.proxy.registerItemRenderer(this,0,"inventory");
	}

}
