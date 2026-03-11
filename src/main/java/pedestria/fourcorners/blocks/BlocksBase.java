package pedestria.fourcorners.blocks;

import net.minecraft.block.Block;
import net.minecraft.block.material.Material;
import net.minecraft.item.Item;
import net.minecraft.item.ItemBlock;
import pedestria.fourcorners.FourCorners;
import pedestria.fourcorners.api.IHasModel;
import pedestria.fourcorners.init.InitBlocks;
import pedestria.fourcorners.init.InitItems;

public class BlocksBase extends Block implements IHasModel {

	public BlocksBase(String name, Material material) {
		super(material);
		setUnlocalizedName(name);
		setRegistryName(name);
		setCreativeTab(FourCorners.fcTab);

		InitBlocks.BLOCKS.add(this);
		InitItems.ITEMS.add(new ItemBlock(this).setRegistryName(this.getRegistryName()));

	}

	@Override
	public void registerModels() {
		FourCorners.proxy.registerItemRenderer(Item.getItemFromBlock(this), 0, "inventory");
	}
	
}
